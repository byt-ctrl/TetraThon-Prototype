import os

# OpenWeatherMap Configuration
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY", "")
OPENWEATHER_BASE_URL = "https://api.openweathermap.org/data/2.5/forecast"
OPENWEATHER_TIMEOUT = 5  # seconds

# Agmarknet / data.gov.in Configuration
AGMARKNET_API_KEY = os.getenv("AGMARKNET_API_KEY", "")
AGMARKNET_BASE_URL = "https://api.data.gov.in/resource"
AGMARKNET_TIMEOUT = 5  # seconds

# Fallback control flags
WEATHER_FALLBACK_ENABLED = True
PRICE_FALLBACK_ENABLED = True
