import math
import time
import datetime
import sys
import requests
import os
import json

def getWeather():
    city = os.environ.get('WEATHER_CITY')
    weatherAPIkey = os.environ.get('OPEN_WEATHER_MAP_API_KEY')
    r = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={weatherAPIkey}&units=metric')
    if not r.ok:
        sys.exit(1)
    print(r.content)
    json.loads(r.content)

testJson = b'{"coord":{"lon":-2.24,"lat":53.48},"weather":[{"id":502,"main":"Rain","description":"heavy intensity rain","icon":"10n"}],"base":"stations","main":{"temp":12.99,"feels_like":12.45,"temp_min":12.22,"temp_max":13.33,"pressure":1012,"humidity":100},"visibility":2600,"wind":{"speed":2.1,"deg":90},"rain":{"1h":1.78},"clouds":{"all":100},"dt":1594244215,"sys":{"type":1,"id":1379,"country":"GB","sunrise":1594180265,"sunset":1594240601},"timezone":3600,"id":2643123,"name":"Manchester","cod":200}'

getWeather()

