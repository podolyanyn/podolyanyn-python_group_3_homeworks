import requests

def weather_app(city):

    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=dbf6455ad98e3999bfaead3775d141eb&units=metric'

    response = requests.get(url)

    if response.status_code == 404:
        return f'"{city}" not found.'

    if response.ok:
        result = response.json()

        temperature = result['main']['temp']
        feels = result['main']['feels_like']
        max_temp = result['main']['temp_max']
        wind_speed = result['wind']['speed']
        sky_status = result['weather'][0]['description']

        return (f'\n Temperature: {temperature}°C\n Feels like: {feels}°C\n The max temperature during the day: {max_temp}°C\n '
              f'The speed of the wind : {wind_speed}m/c\n The sky status: {sky_status}\n')
    else:
        return 'Error:', response.status_code

if __name__ == '__main__':
    while True:
        input_city = input('Enter a city to get current weather: ')
        print(weather_app(input_city))