import os
import sys

# Ensure UTF-8 output encoding for Windows terminal
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from pathlib import Path
backend_dir = Path(__file__).resolve().parent
sys.path.insert(0, str(backend_dir))

from unittest.mock import patch, MagicMock
from App.adapters.weather import get_forecast, _parse_owm_forecast, LOCATION_COORDS


def test_milestone_3_location_validation():
    print("Testing Milestone 3: Location Input Validation...")
    try:
        get_forecast("")
        assert False, "Expected ValueError on empty location"
    except ValueError:
        print("  [OK] Empty location correctly raised ValueError")

    try:
        get_forecast("InvalidCityName")
        assert False, "Expected ValueError on unknown location"
    except ValueError:
        print("  [OK] Unknown location correctly raised ValueError")


def test_milestone_3_all_seeded_locations():
    print("\nTesting Milestone 3: All Seeded Locations Output Structure...")
    locations = ["Ahmedabad", "Vadodara", "Surat", "Rajkot", "Anand"]
    for loc in locations:
        res = get_forecast(loc)
        assert res["location"] == loc
        assert "forecast" in res
        assert len(res["forecast"]) == 7
        assert "source" in res
        
        # Verify first day structure
        day1 = res["forecast"][0]
        required_keys = ["day", "date", "temp_high", "temp_low", "rain_chance", "humidity", "wind_kph"]
        for key in required_keys:
            assert key in day1, f"Missing key {key} in forecast item"
        print(f"  [OK] {loc}: 7-day forecast valid (source={res['source']})")


def test_milestone_3_owm_parser():
    print("\nTesting Milestone 3: OpenWeatherMap Response Parser...")
    sample_owm_data = {
        "list": [
            {
                "dt_txt": "2026-07-23 09:00:00",
                "main": {"temp": 32.5, "humidity": 65},
                "wind": {"speed": 4.5},
                "pop": 0.2
            },
            {
                "dt_txt": "2026-07-23 12:00:00",
                "main": {"temp": 36.0, "humidity": 55},
                "wind": {"speed": 5.0},
                "pop": 0.4
            },
            {
                "dt_txt": "2026-07-24 09:00:00",
                "main": {"temp": 30.0, "humidity": 70},
                "wind": {"speed": 3.0},
                "pop": 0.1
            }
        ]
    }
    
    parsed = _parse_owm_forecast(sample_owm_data)
    assert len(parsed) == 2
    assert parsed[0]["day"] == 1
    assert parsed[0]["date"] == "2026-07-23"
    assert parsed[0]["temp_high"] == 36
    assert parsed[0]["temp_low"] == 32
    assert parsed[0]["rain_chance"] == 30  # Average of 20% and 40%
    print("  [OK] OWM response parser correctly aggregated daily forecasts.")


def test_milestone_3_mocked_live_fetch():
    print("\nTesting Milestone 3: Live API Fetch Workflow (Mocked HTTP)...")
    mock_resp = MagicMock()
    mock_resp.raise_for_status = MagicMock()
    mock_resp.json = MagicMock(return_value={
        "list": [
            {
                "dt_txt": "2026-07-23 12:00:00",
                "main": {"temp": 35.0, "humidity": 60},
                "wind": {"speed": 4.0},
                "pop": 0.1
            }
        ]
    })

    with patch("App.adapters.weather.OPENWEATHER_API_KEY", "valid_test_api_key"):
        with patch("httpx.Client.get", return_value=mock_resp):
            res = get_forecast("Ahmedabad")
            assert res["source"] == "live"
            assert res["location"] == "Ahmedabad"
            print("  [OK] Live API fetch returned source='live' when API key is set.")


if __name__ == "__main__":
    print("=== STARTING MILESTONE 3 VERIFICATION ===")
    test_milestone_3_location_validation()
    test_milestone_3_all_seeded_locations()
    test_milestone_3_owm_parser()
    test_milestone_3_mocked_live_fetch()
    print("\n=== MILESTONE 3 VERIFICATION COMPLETED SUCCESSFULLY! ===")
