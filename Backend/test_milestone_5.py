import sys
import os

# Ensure UTF-8 output encoding for Windows terminal
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from pathlib import Path
backend_dir = Path(__file__).resolve().parent
sys.path.insert(0, str(backend_dir))

from unittest.mock import patch, MagicMock
from App.adapters.market_prices import (
    load_prices, get_latest_price, get_future_price, get_price_adapter_status, MARKET_IDS
)
from App.engine.decision import generate_recommendation


def test_milestone_5_market_ids():
    print("Testing Milestone 5: APMC Market ID Mappings...")
    expected_markets = ["Ahmedabad APMC", "Vadodara APMC", "Surat APMC", "Rajkot APMC", "Anand APMC"]
    for m in expected_markets:
        assert m in MARKET_IDS, f"Missing market mapping for {m}"
        assert MARKET_IDS[m].startswith("GJ"), f"Invalid APMC code format for {m}"
    print(f"  [OK] All {len(expected_markets)} APMC market IDs mapped correctly.")


def test_milestone_5_all_crops_and_markets():
    print("\nTesting Milestone 5: Price Lookups for 4 Crops x 5 Markets...")
    crops = ["Cotton", "Wheat", "Groundnut", "Tomato"]
    markets = ["Ahmedabad APMC", "Vadodara APMC", "Surat APMC", "Rajkot APMC", "Anand APMC"]
    
    count = 0
    for crop in crops:
        for market in markets:
            series = load_prices(crop, market)
            assert len(series) > 0, f"Empty price series for {crop} at {market}"
            latest = get_latest_price(crop, market)
            future_7 = get_future_price(crop, market, 7)
            future_14 = get_future_price(crop, market, 14)
            
            assert latest > 0, f"Latest price <= 0 for {crop} at {market}"
            assert future_7 > 0, f"7-day future price <= 0 for {crop} at {market}"
            assert future_14 > 0, f"14-day future price <= 0 for {crop} at {market}"
            count += 1
            
    print(f"  [OK] Successfully validated {count} crop-market price series.")


def test_milestone_5_mocked_live_fetch():
    print("\nTesting Milestone 5: Live Agmarknet/data.gov.in API Fetch (Mocked HTTP)...")
    mock_resp = MagicMock()
    mock_resp.raise_for_status = MagicMock()
    mock_resp.json = MagicMock(return_value={
        "records": [
            {"date": "2026-07-20", "modal_price": "6200"},
            {"date": "2026-07-21", "modal_price": "6250"},
            {"date": "2026-07-22", "modal_price": "6300"}
        ]
    })

    with patch("App.adapters.market_prices.AGMARKNET_API_KEY", "valid_test_agmarknet_key"):
        with patch("httpx.Client.get", return_value=mock_resp):
            series = load_prices("Cotton", "Ahmedabad APMC")
            assert len(series) == 3
            assert series[0]["price"] == 6200.0
            assert series[2]["price"] == 6300.0
            status = get_price_adapter_status("Cotton", "Ahmedabad APMC")
            assert status == "live"
            print("  [OK] Live price fetch returned parsed records and source='live'.")


def test_milestone_5_decision_engine_integration():
    print("\nTesting Milestone 5: Integration with Post-Harvest Decision Engine...")
    rec = generate_recommendation("Wheat", 100.0, "cold_storage", 23.0225, 72.5714)
    assert "recommendation" in rec
    assert rec["recommendation"] in ["sell_now", "store", "transport"]
    assert rec["expected_return"] > 0
    print(f"  [OK] Post-harvest decision output verified: {rec['option_label']} (INR {rec['expected_return']}).")


if __name__ == "__main__":
    print("=== STARTING MILESTONE 5 VERIFICATION ===")
    test_milestone_5_market_ids()
    test_milestone_5_all_crops_and_markets()
    test_milestone_5_mocked_live_fetch()
    test_milestone_5_decision_engine_integration()
    print("\n=== MILESTONE 5 VERIFICATION COMPLETED SUCCESSFULLY! ===")
