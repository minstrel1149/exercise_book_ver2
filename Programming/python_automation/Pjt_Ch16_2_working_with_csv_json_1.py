import json
import requests
import sys
from pathlib import Path
import pyinputplus as pyip

if len(sys.argv) < 2:
    print('Usage: Pjt_Ch16_2_working_with_csv_json_1.py latitude logitude apikey')
    sys.exit()

lat = sys.argv[2]
lon = sys.argv[3]

apikey = sys.argv[1]

url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={apikey}'
res = requests.get(url)
res.raise_for_status()

weatherData = json.loads(res.text)

print(f'Current weather in {weatherData["name"]}')
print(weatherData['weather'][0]['main'], '-', weatherData['weather'][0]['description'])