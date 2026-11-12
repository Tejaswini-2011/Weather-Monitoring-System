import os

try:
    from secrets_local import API_KEY
except ImportError:
    API_KEY = os.getenv("OPENWEATHER_API_KEY", "")

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
