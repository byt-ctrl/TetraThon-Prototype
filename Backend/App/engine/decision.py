import os
import csv

CSV_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "data", "mandi_prices.csv"))

# Module-level cache: key is (crop, market), value is list of {"date": date, "price": price, "price_per_quintal": price}
_prices_cache = {}

def load_prices(crop: str, market: str) -> list[dict]:
    """
    Reads the mandi_prices.csv file, filters by the specified crop and market,
    and returns a list of dictionaries with 'date' and 'price' / 'price_per_quintal'
    sorted by date ascending. Uses module-level caching for performance.
    """
    cache_key = (crop, market)
    if cache_key in _prices_cache:
        return _prices_cache[cache_key]
        
    if not os.path.exists(CSV_PATH):
        raise FileNotFoundError(f"CSV file not found at {CSV_PATH}")
        
    # If cache is empty, load everything in one pass to populate the cache
    if not _prices_cache:
        with open(CSV_PATH, mode="r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                key = (row["crop"], row["market"])
                price_val = float(row["price_per_quintal"])
                if key not in _prices_cache:
                    _prices_cache[key] = []
                _prices_cache[key].append({
                    "date": row["date"],
                    "price": price_val,
                    "price_per_quintal": price_val
                })
        
        # Sort each list by date
        for key in _prices_cache:
            _prices_cache[key].sort(key=lambda x: x["date"])
            
    # Return the cached list, default to empty list if not found
    return _prices_cache.get(cache_key, [])
