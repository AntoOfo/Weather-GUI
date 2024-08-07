import requests
from datetime import datetime
import pytz


api_key = "dd983f4b06532bc0823252920cd8d1ec"

city_to_timezone = {
    "London": "Europe/London",
    "New York": "America/New_York",
    "Dublin": "Europe/Dublin",
    "Tokyo": "Asia/Tokyo",
    "Sydney": "Australia/Sydney",
    "Paris": "Europe/Paris"
}
while True:
    try:
        user_input = input("Enter city: ").strip().title()


        response = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=metric&appid={api_key}"
        )
        data = response.json()
        weather = data["weather"][0]["main"]
        temp = round(data["main"]["temp"])
        windspeed = data["wind"]["speed"]


        timezone_name = city_to_timezone.get(user_input)



        if timezone_name is None:
            city_time = "Unknown"
            city_date = "Unknown"
        else:
            timezone = pytz.timezone(timezone_name)
            now = datetime.now(timezone)
            city_time = now.strftime("%H:%M")
            city_date = now.strftime("%m-%d")


        print(f"City entered is {user_input}")
        print(f"Weather is {weather}")
        print(f"Temperature is {temp}C")
        print(f"Time is {city_time}")
        print(f"Date is {city_date}")
        print(f"Wind speed is {windspeed}")
    except KeyError:
        print("Invalid Input")
        continue
    