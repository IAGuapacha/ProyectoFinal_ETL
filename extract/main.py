import requests
import os

KEY_WEATHERAPI = os.getenv("KEY_WEATHERAPI")
print(KEY_WEATHERAPI)
response = requests.get(
    'http://api.weatherapi.com/v1/current.json',
    params={'key': KEY_WEATHERAPI,
            'q': 'Bogota',
            'lang': 'es'})
json_response = response.json()
print(json_response)
