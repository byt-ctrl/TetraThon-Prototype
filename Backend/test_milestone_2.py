import os
import sys
from pathlib import Path

# Ensure UTF-8 output encoding for Windows terminal
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

backend_dir = Path(__file__).resolve().parent
sys.path.insert(0, str(backend_dir))


def test_milestone_2_defaults():
    print("Testing Milestone 2: Default Config Values...")
    import App.adapters.config as config
    
    assert hasattr(config, "OPENWEATHER_API_KEY"), "Missing OPENWEATHER_API_KEY"
    assert hasattr(config, "OPENWEATHER_BASE_URL"), "Missing OPENWEATHER_BASE_URL"
    assert hasattr(config, "OPENWEATHER_TIMEOUT"), "Missing OPENWEATHER_TIMEOUT"
    assert hasattr(config, "AGMARKNET_API_KEY"), "Missing AGMARKNET_API_KEY"
    assert hasattr(config, "AGMARKNET_BASE_URL"), "Missing AGMARKNET_BASE_URL"
    assert hasattr(config, "AGMARKNET_TIMEOUT"), "Missing AGMARKNET_TIMEOUT"
    assert hasattr(config, "WEATHER_FALLBACK_ENABLED"), "Missing WEATHER_FALLBACK_ENABLED"
    assert hasattr(config, "PRICE_FALLBACK_ENABLED"), "Missing PRICE_FALLBACK_ENABLED"
    
    assert config.OPENWEATHER_TIMEOUT == 5
    assert config.AGMARKNET_TIMEOUT == 5
    assert config.WEATHER_FALLBACK_ENABLED is True
    assert config.PRICE_FALLBACK_ENABLED is True
    print("  [OK] Default values verified successfully.")


def test_milestone_2_env_overrides():
    print("\nTesting Milestone 2: Environment Variable Overrides...")
    os.environ["OPENWEATHER_API_KEY"] = "test_owm_key_123"
    os.environ["AGMARKNET_API_KEY"] = "test_agmarknet_key_456"
    os.environ["OPENWEATHER_TIMEOUT"] = "10"
    
    # Reload module to pick up env vars
    import importlib
    import App.adapters.config as config
    importlib.reload(config)
    
    assert config.OPENWEATHER_API_KEY == "test_owm_key_123"
    assert config.AGMARKNET_API_KEY == "test_agmarknet_key_456"
    assert config.OPENWEATHER_TIMEOUT == 10
    print("  [OK] Environment variable overrides verified successfully.")


if __name__ == "__main__":
    print("=== STARTING MILESTONE 2 VERIFICATION ===")
    test_milestone_2_defaults()
    test_milestone_2_env_overrides()
    print("\n=== MILESTONE 2 VERIFICATION COMPLETED SUCCESSFULLY! ===")
