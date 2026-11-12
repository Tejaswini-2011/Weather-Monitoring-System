def save_weather(weather_data):
    with open("weather_log.txt", "a") as file:
        file.write(
            f"{weather_data['name']} | "
            f"{weather_data['main']['temp']}°C | "
            f"{weather_data['weather'][0]['description']}\n"
        )