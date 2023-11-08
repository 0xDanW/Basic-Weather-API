# file deepcode ignore HardcodedNonCryptoSecret: <please specify a reason of ignoring this>
import os
import requests

# fmt: off
API_KEY = "59251a9f36c9236bca9ceaeb377adef3"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
# fmt: on

city = input("Enter a city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data["weather"][0]["description"]
    print(f"Weather: {weather}")
    temperature = round(data["main"]["temp"] - 273.15, 2)
    print(f"Temperature: {temperature} degrees")
else:
    print("ERROR: An error occured!")
