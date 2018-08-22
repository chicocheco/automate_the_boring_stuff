#! python3
# json_weather.py - Prints the weather for a location from the command line.
# http://api.openweathermap.org/data/2.5/forecast?q=San+Francisco,us&appid=68b3edb9c8bd2e83fa57a4d0fcb6e610

import json
import requests
import sys

# Compute location from command line arguments.
api_key = '68b3edb9c8bd2e83fa57a4d0fcb6e610'

if len(sys.argv) < 2:
    print('Usage: quickWeather.py location')
    sys.exit()

# Create just one long string from the input text.
location = ' '.join(sys.argv[1:])

# Download the JSON email_data from OpenWeatherMap.org's API.

url = f'http://api.openweathermap.org/email_data/2.5/forecast?q={location}&units=metric&appid={api_key}'
response = requests.get(url)
response.raise_for_status()

# Load JSON email_data into a Python variable - dictionary type.
weather_data = json.loads(response.text)

# Get the key-value (list) of the key named 'list'.
w = weather_data['list']

print(f'Current weather in {location}:')
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print('Temperature: ', w[0]['main']['temp'], ' °C')
print()

print('Tomorrow:')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print('Minimum temperature: ', w[1]['main']['temp_min'], ' °C')
print('Maximum temperature: ', w[1]['main']['temp_max'], ' °C')
print()

print('Day after tomorrow:')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])
print('Minimum temperature: ', w[2]['main']['temp_min'], ' °C')
print('Maximum temperature: ', w[2]['main']['temp_max'], ' °C')


