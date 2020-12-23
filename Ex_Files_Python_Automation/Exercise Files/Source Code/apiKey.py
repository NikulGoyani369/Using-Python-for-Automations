import requests

baseUrl = 'http://api.openweathermap.org/data/2.5/forecast'
parameters = {'APPID':'put your api key here',  'q':'Seattle,US'}
response = requests.get(baseUrl, params=parameters)
print(response.content)
