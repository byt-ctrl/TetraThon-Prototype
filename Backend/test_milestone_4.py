import sys
import os

# Ensure UTF-8 output encoding for Windows terminal
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from pathlib import Path
backend_dir = Path(__file__).resolve().parent
sys.path.insert(0, str(backend_dir))

from unittest.mock import patch, MagicMock
import httpx
from App.adapters.weather import get_forecast


def test_fallback_no_api_key():
    print("Testing Milestone 4: Fallback Scenario 1 — No API Key Set...")
    with patch("App.adapters.weather.OPENWEATHER_API_KEY", ""):
        res = get_forecast("Ahmedabad")
        assert res["location"] == "Ahmedabad"
        assert res["source"] == "mock"
        assert len(res["forecast"]) == 7
        print("  [OK] Successfully fell back to mock forecast when OPENWEATHER_API_KEY is empty.")


def test_fallback_invalid_api_key_401():
    print("\nTesting Milestone 4: Fallback Scenario 2 — Invalid API Key (HTTP 401)...")
    mock_resp = MagicMock()
    mock_resp.raise_for_status.side_effect = httpx.HTTPStatusError("401 Unauthorized", request=MagicMock(), response=mock_resp)

    with patch("App.adapters.weather.OPENWEATHER_API_KEY", "invalid_api_key_xyz"):
        with patch("httpx.Client.get", return_value=mock_resp):
            res = get_forecast("Vadodara")
            assert res["location"] == "Vadodara"
            assert res["source"] == "mock"
            assert len(res["forecast"]) == 7
            print("  [OK] Successfully fell back to mock forecast on HTTP 401 Unauthorized.")


def test_fallback_server_error_500():
    print("\nTesting Milestone 4: Fallback Scenario 3 — OpenWeather Server Error (HTTP 500)...")
    mock_resp = MagicMock()
    mock_resp.raise_for_status.side_effect = httpx.HTTPStatusError("500 Internal Server Error", request=MagicMock(), response=mock_resp)

    with patch("App.adapters.weather.OPENWEATHER_API_KEY", "some_key"):
        with patch("httpx.Client.get", return_value=mock_resp):
            res = get_forecast("Surat")
            assert res["location"] == "Surat"
            assert res["source"] == "mock"
            assert len(res["forecast"]) == 7
            print("  [OK] Successfully fell back to mock forecast on HTTP 500 Internal Server Error.")


def test_fallback_timeout():
    print("\nTesting Milestone 4: Fallback Scenario 4 — Network Timeout (>5s)...")
    with patch("App.adapters.weather.OPENWEATHER_API_KEY", "some_key"):
        with patch("httpx.Client.get", side_effect=httpx.TimeoutException("Connection timed out")):
            res = get_forecast("Rajkot")
            assert res["location"] == "Rajkot"
            assert res["source"] == "mock"
            assert len(res["forecast"]) == 7
            print("  [OK] Successfully fell back to mock forecast on TimeoutException.")


def test_fallback_malformed_json():
    print("\nTesting Milestone 4: Fallback Scenario 5 — Malformed Response JSON...")
    mock_resp = MagicMock()
    mock_resp.raise_for_status = MagicMock()
    mock_resp.json = MagicMock(return_value={"invalid_schema": True})

    with patch("App.adapters.weather.OPENWEATHER_API_KEY", "some_key"):
        with patch("httpx.Client.get", return_value=mock_resp):
            res = get_forecast("Anand")
            assert res["location"] == "Anand"
            assert res["source"] == "mock"
            assert len(res["forecast"]) == 7
            print("  [OK] Successfully fell back to mock forecast on malformed JSON response.")


if __name__ == "__main__":
    print("=== STARTING MILESTONE 4 VERIFICATION ===")
    test_fallback_no_api_key()
    test_fallback_invalid_api_key_401()
    test_fallback_server_error_500()
    test_fallback_timeout()
    test_fallback_malformed_json()
    print("\n=== MILESTONE 4 VERIFICATION COMPLETED SUCCESSFULLY! ===")
