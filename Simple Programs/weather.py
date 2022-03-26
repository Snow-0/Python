# Simple CLI based weather checker
# Enter a city and this will return the temperature in Fahrenheit and the description of the city

import json
import requests

city = input("What city would you like to search for? ")
api_key = "2cd79f8ae3fa5cca37f4cfa4ba0add32"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=imperial"



response = requests.get(url)
weather_data = response.json()
# Program ends when given an invalid city
if weather_data["cod"] == "404":
    print("Invalid city, please try again")
# Prints the weather
else: 
    print("City: " + weather_data["name"])
    print("Temperature: " + str(weather_data["main"]["temp"]) + "F")
    print("Lows: " + str(weather_data["main"]["temp_min"])+ "F")
    print("Highs: " + str(weather_data["main"]["temp_max"]) + "F")
    # weather is a list that has one dictionary, so index 0 is needed
    print("Description: " + weather_data["weather"][0]["description"])