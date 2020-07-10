import math
import time
import datetime
import sys
import requests
import os
import json

from os.path import join, dirname
from dotenv import load_dotenv
 
# Create .env file path.
dotenv_path = join(dirname(__file__), '.env')
 
# Load file from the path.
load_dotenv(dotenv_path)

def getWeather():
    city = os.environ.get('WEATHER_CITY')
    weatherAPIkey = os.environ.get('OPEN_WEATHER_MAP_API_KEY')
    r = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={weatherAPIkey}&units=metric')
    if not r.ok:
        sys.exit(1)
    weatherData = json.loads(r.content)

    weatherDescription = weatherData["weather"][0]
    figures = weatherData["main"]
    # rainInfo = weatherData["rain"]
    systemInfo = weatherData["sys"]

    currentWeatherShort = weatherDescription["main"]
    currentWeatherLong = weatherDescription["description"]
    currentWeatherIcon = weatherDescription["icon"]
    
    temperature = figures["temp"]
    feels_like = figures["feels_like"]

    sunriseUTC = systemInfo["sunrise"]
    sunsetUTC = systemInfo["sunset"]

    locationName = weatherData["name"]

    print(f"{currentWeatherShort} ({currentWeatherLong}) in {locationName}")
