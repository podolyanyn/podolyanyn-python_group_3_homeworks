import requests

API_KEY = '5a8c4c1b52c84775b7164735252309'
responce = requests.get(f'http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={input('Pls enter a city for weather info: ')}&lang=uk')

for key, value in responce.json().items():
    print(f'{key}: {value}')