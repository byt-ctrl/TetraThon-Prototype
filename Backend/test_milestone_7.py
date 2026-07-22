import sys
import os

# Ensure UTF-8 output encoding for Windows terminal
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from pathlib import Path
backend_dir = Path(__file__).resolve().parent
sys.path.insert(0, str(backend_dir))

from unittest.mock import patch, MagicMock
from fastapi.testclient import TestClient
from App.main import app
from App.routers.health import health

client = TestClient(app)


def test_milestone_7_direct_health_function():
    print("Testing Milestone 7: Direct health() Function Invocation...")
    res = health()
    assert res["status"] == "OK"
    assert res["version"] == "1.0.0-phase1"
    assert "adapters" in res
    assert "weather" in res["adapters"]
    assert "prices" in res["adapters"]
    assert res["adapters"]["weather"] in ["live", "mock"]
    assert res["adapters"]["prices"] in ["live", "mock"]
    print(f"  [OK] health() returned valid structure: {res}")


def test_milestone_7_http_endpoint():
    print("\nTesting Milestone 7: HTTP GET /api/health via FastAPI TestClient...")
    response = client.get("/api/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "OK"
    assert "adapters" in data
    assert "weather" in data["adapters"]
    assert "prices" in data["adapters"]
    print(f"  [OK] GET /api/health HTTP 200 OK: {data}")


def test_milestone_7_live_adapters_reported():
    print("\nTesting Milestone 7: Health Endpoint Live vs Mock Reporting...")
    
    mock_weather = {"location": "Ahmedabad", "forecast": [], "source": "live"}
    
    with patch("App.routers.health.get_forecast", return_value=mock_weather):
        with patch("App.routers.health.get_price_adapter_status", return_value="live"):
            res = health()
            assert res["adapters"]["weather"] == "live"
            assert res["adapters"]["prices"] == "live"
            print("  [OK] Health endpoint correctly reported both adapters as 'live'.")

    with patch("App.routers.health.get_forecast", return_value={"location": "Ahmedabad", "forecast": [], "source": "mock"}):
        with patch("App.routers.health.get_price_adapter_status", return_value="mock"):
            res = health()
            assert res["adapters"]["weather"] == "mock"
            assert res["adapters"]["prices"] == "mock"
            print("  [OK] Health endpoint correctly reported both adapters as 'mock'.")


if __name__ == "__main__":
    print("=== STARTING MILESTONE 7 VERIFICATION ===")
    test_milestone_7_direct_health_function()
    test_milestone_7_http_endpoint()
    test_milestone_7_live_adapters_reported()
    print("\n=== MILESTONE 7 VERIFICATION COMPLETED SUCCESSFULLY! ===")
