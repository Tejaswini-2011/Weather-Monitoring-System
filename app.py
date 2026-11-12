import json
from fastapi import FastAPI
from weather_service import get_weather
from alert_service import check_alert
from history_service import save_history

app = FastAPI()


@app.get("/weather/{city}")
def get_city_weather(city: str):

    weather_data = get_weather(city)

    if weather_data and weather_data["cod"] == 200:

        alert = check_alert(weather_data)

        save_history(weather_data)

        return {
            "city": weather_data["name"],
            "temperature": weather_data["main"]["temp"],
            "humidity": weather_data["main"]["humidity"],
            "weather": weather_data["weather"][0]["description"],
            "wind_speed": weather_data["wind"]["speed"],
            "alerts": alert
        }

    return {
        "error": "Unable to fetch weather data"
    }


@app.get("/history")
def get_history():

    with open("weather_history.json", "r") as file:
        history = json.load(file)

    return history