def check_alert(weather_data):

    alerts = []

    temp = weather_data["main"]["temp"]
    weather = weather_data["weather"][0]["main"]
    wind_speed = weather_data["wind"]["speed"]

    if temp > 40:
        alerts.append("HEAT ALERT! Temperature above 40°C")

    elif temp > 35:
        alerts.append("HOT WEATHER ALERT!")

    if weather == "Rain":
        alerts.append("RAIN ALERT! Carry an umbrella")

    if wind_speed > 10:
        alerts.append("WIND ALERT! Strong winds detected")

    return alerts