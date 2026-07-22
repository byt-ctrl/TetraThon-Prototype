import sys
import os
from pathlib import Path

# Ensure UTF-8 output encoding for Windows terminal stdout
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

# Ensure Backend directory is in python path
backend_dir = Path(__file__).resolve().parent
sys.path.insert(0, str(backend_dir))

from App.adapters.config import OPENWEATHER_API_KEY, AGMARKNET_API_KEY
from App.adapters.weather import get_forecast
from App.adapters.market_prices import load_prices, get_latest_price, get_future_price, get_price_adapter_status
from App.engine.decision import generate_recommendation
from App.routers.health import health


def test_weather_adapter():
    print("Testing Weather Adapter...")
    locations = ["Ahmedabad", "Vadodara", "Surat", "Rajkot", "Anand"]
    for loc in locations:
        res = get_forecast(loc)
        assert res["location"] == loc
        assert len(res["forecast"]) == 7
        assert "source" in res
        print(f"  [OK] {loc}: source={res['source']}, days={len(res['forecast'])}")


def test_market_prices_adapter():
    print("\nTesting Market Prices Adapter...")
    crops = ["Cotton", "Wheat", "Groundnut", "Tomato"]
    markets = ["Ahmedabad APMC", "Vadodara APMC", "Surat APMC", "Rajkot APMC", "Anand APMC"]
    
    for crop in crops:
        for market in markets:
            prices = load_prices(crop, market)
            assert len(prices) > 0, f"No prices for {crop} at {market}"
            latest = get_latest_price(crop, market)
            future = get_future_price(crop, market, 14)
            assert latest > 0, f"Latest price 0 for {crop} at {market}"
            assert future > 0, f"Future price 0 for {crop} at {market}"
    print(f"  [OK] Tested {len(crops)} crops x {len(markets)} markets successfully")


def test_decision_engine():
    print("\nTesting Decision Engine Integration...")
    rec = generate_recommendation("Cotton", 50.0, "warehouse", 23.0225, 72.5714)
    assert "recommendation" in rec
    assert rec["expected_return"] > 0
    print(f"  [OK] Decision recommendation: {rec['recommendation']} ({rec['option_label']}) - Return: INR {rec['expected_return']}")


def test_health_endpoint():
    print("\nTesting Health Endpoint...")
    h = health()
    assert h["status"] == "OK"
    assert "adapters" in h
    assert "weather" in h["adapters"]
    assert "prices" in h["adapters"]
    print(f"  [OK] Health response: {h}")


if __name__ == "__main__":
    print("=== STARTING CHUNK 5 VERIFICATION TESTS ===")
    test_weather_adapter()
    test_market_prices_adapter()
    test_decision_engine()
    test_health_endpoint()
    print("\n=== ALL CHUNK 5 VERIFICATION TESTS PASSED SUCCESSFULLY! ===")
