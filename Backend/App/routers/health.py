from fastapi import APIRouter
from ..adapters.weather import get_forecast
from ..adapters.market_prices import get_price_adapter_status

router = APIRouter()


@router.get("/health")
def health():
    # Test weather adapter status
    try:
        test_weather = get_forecast("Ahmedabad")
        weather_source = test_weather.get("source", "unknown")
    except Exception:
        weather_source = "error"
    
    # Test price adapter status
    try:
        price_source = get_price_adapter_status("Cotton", "Ahmedabad APMC")
    except Exception:
        price_source = "error"

    return {
        "status": "OK",
        "version": "1.0.0-phase1",
        "adapters": {
            "weather": weather_source,
            "prices": price_source
        }
    }
