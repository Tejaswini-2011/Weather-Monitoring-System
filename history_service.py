import json
import os
from datetime import datetime

FILE_NAME = "weather_history.json"


def save_history(weather_data):

    record = {
        "city": weather_data["name"],
        "temperature": weather_data["main"]["temp"],
        "weather": weather_data["weather"][0]["description"],
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            history = json.load(file)
    else:
        history = []

    history.append(record)

    with open(FILE_NAME, "w") as file:
        json.dump(history, file, indent=4)