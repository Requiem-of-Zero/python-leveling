import requests, json
city_name = 'San Francisco'
state_code = 'CA'
country_code = 'US'
API_key = '6db911c4abd77469b2b375b3f5f7745d'  # Not a real API key
response = requests.get(f'https://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&appid={API_key}')
response_data = json.loads(response.text)
lat = response_data[0]['lat']
lon = response_data[0]['lon']  # This is a Python string.
response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}')
response_data = json.loads(response.text)
print(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}')
print(round(response_data['main']['temp'] * (9/5) - 459.67, 1))