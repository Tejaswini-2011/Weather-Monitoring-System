from weather_service import get_weather
from alert_service import check_alert
from weather_logger import save_weather

city = input("Enter city name: ")

weather_data = get_weather(city)

if weather_data and weather_data["cod"] == 200:
    print("\n===== WEATHER REPORT =====")
    print("City:", weather_data["name"])
    print("Temperature:", weather_data["main"]["temp"], "°C")
    print("Humidity:", weather_data["main"]["humidity"], "%")
    print("Weather:", weather_data["weather"][0]["description"])
    print("Wind Speed:", weather_data["wind"]["speed"], "m/s")

    check_alert(weather_data)
    print("Weather data saved successfully!")

else:
    print("Unable to fetch weather data")