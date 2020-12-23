import requests

baseUrl = 'http://api.openweathermap.org/data/2.5/forecast'
parameters = {'APPID':'1bfbdd122940b0f6fad3a06b1376b377',  'q':'Seattle,US'}
response = requests.get(baseUrl, params=parameters)
print(response.content)
