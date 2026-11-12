# Weather Monitoring System

A Python app that fetches live weather for any city from the [OpenWeatherMap API](https://openweathermap.org/api), raises alerts for extreme conditions, and keeps a history of past lookups.

It can be used two ways:

- **REST API** built with FastAPI (`app.py`)
- **Command-line tool** (`main.py`)

## Features

- Current temperature, humidity, weather description and wind speed for any city
- Weather alerts:
  | Condition | Alert |
  |---|---|
  | Temperature above 40°C | `HEAT ALERT! Temperature above 40°C` |
  | Temperature above 35°C | `HOT WEATHER ALERT!` |
  | Rain | `RAIN ALERT! Carry an umbrella` |
  | Wind speed above 10 m/s | `WIND ALERT! Strong winds detected` |
- Every API lookup is saved to `weather_history.json` with a timestamp

## Project structure

```
weather-alert-app/
├── app.py               # FastAPI app: /weather/{city} and /history endpoints
├── main.py              # Command-line version
├── weather_service.py   # Calls the OpenWeatherMap API
├── alert_service.py     # Checks weather data and builds alerts
├── history_service.py   # Saves lookups to weather_history.json
├── weather_logger.py    # Appends lookups to weather_log.txt
├── config.py            # Loads the API key and base URL
└── weather_history.json # Saved lookup history
```

## Getting started

### 1. Clone the repository

```bash
git clone https://github.com/Tejaswini-2011/Weather-Monitoring-System.git
cd Weather-Monitoring-System
```

### 2. Install dependencies

Requires Python 3.8+.

```bash
pip install fastapi uvicorn requests
```

### 3. Add your API key

1. Sign up at [home.openweathermap.org](https://home.openweathermap.org/) and copy your API key from the **API keys** tab.
2. Provide the key in **one** of these ways:

   **Option A:** create a file called `secrets_local.py` in the project folder:

   ```python
   API_KEY = "your_api_key_here"
   ```

   **Option B:** set an environment variable:

   ```bash
   # Windows (PowerShell)
   $env:OPENWEATHER_API_KEY = "your_api_key_here"

   # macOS / Linux
   export OPENWEATHER_API_KEY="your_api_key_here"
   ```

`secrets_local.py` is listed in `.gitignore`, so your key is never committed.

> New OpenWeatherMap keys can take a little while to activate. If you get a `401` error at first, wait and try again.

## Usage

### Run the API

```bash
uvicorn app:app --reload
```

The API runs at `http://127.0.0.1:8000`. Interactive docs are at `http://127.0.0.1:8000/docs`.

#### `GET /weather/{city}`

Returns current weather and any alerts for a city, and saves the lookup to history.

```
GET http://127.0.0.1:8000/weather/Hyderabad
```

```json
{
  "city": "Hyderabad",
  "temperature": 37.01,
  "humidity": 30,
  "weather": "clear sky",
  "wind_speed": 4.1,
  "alerts": ["HOT WEATHER ALERT!"]
}
```

If the city is not found or the request fails:

```json
{ "error": "Unable to fetch weather data" }
```

#### `GET /history`

Returns all saved lookups.

```json
[
  {
    "city": "Hyderabad",
    "temperature": 37.01,
    "weather": "clear sky",
    "timestamp": "2026-06-17 12:40:22"
  }
]
```

### Run from the command line

```bash
python main.py
```

```
Enter city name: Hyderabad

===== WEATHER REPORT =====
City: Hyderabad
Temperature: 37.01 °C
Humidity: 30 %
Weather: clear sky
Wind Speed: 4.1 m/s
```

## Tech stack

- Python
- FastAPI and Uvicorn
- Requests
- OpenWeatherMap Current Weather API
