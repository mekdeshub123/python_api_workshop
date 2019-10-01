import requests

url = 'https://api.weather.gov/gridpoints/MPX/107,71/forecast'

response = requests.get(url).json()
forecast_periods = response['properties']['periods']

for period in forecast_periods:
    day = period['name']
    temp = period['temperature']
    forecast = period['detailedForecast']
    print(f'{day}: {temp}F. {forecast}\n')


