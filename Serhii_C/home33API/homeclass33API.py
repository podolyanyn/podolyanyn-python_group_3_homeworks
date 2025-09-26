# Завдання 1
#
# Robots.txt
#
# Завантажте та збережіть у файл robots.txt з Вікіпедії, веб-сайтів Twitter тощо.
# import sqlite3
# import requests
# from datetime import datetime
# base_url = f'https://w.wiki/4wJS'
# headers = {
#     'User-Agent': 'My WikiBot/1.0 (MyName@example.com)'
# }
# response = requests.get(base_url,headers=headers)
# response.decoding = 'utf-8'
# with open('robot.txt', 'wb') as f:
#     f.write(response.content)
import pandas as pd
# Завдання 2
#
# Завантаження даних
#
# Завантажте всі коментарі з вибраного вами subreddit за допомогою URL-адреси:
# https://api.pushshift.io/reddit/comment/search/ .
# В результаті збережіть усі коментарі в хронологічному порядку у форматі
# JSON та виведіть їх у файл.
#Замість комментарів зберіг дані про зовнішній борг у форматі JSON

# import requests
# import json
#
# def fetch_nbu_data(start,end):
#     """Отримання даних з API НБУ"""
#     base_url = f"https://bank.gov.ua/NBUStatService/v1/statdirectory/grossextdebt?{start}=20160301&{end}=20170601&json"
#
#     response = requests.get(base_url)
#     return response.json()
#
# data_for_save = fetch_nbu_data(20220517,20250701)
# print(data_for_save)
# with open("data_for_save.json", "w", encoding="utf-8") as f:
#     json.dump(data_for_save, f, ensure_ascii=False, indent=4)

# Завдання 3
#
# Додаток «Погода»
#
# Напишіть консольний додаток, який приймає на вхід назву міста та повертає поточну погоду у вибраному вами форматі.
# Для поточного завдання ви можете вибрати будь-який API погоди чи вебсайт, або скористатися openweathermap.org.



import requests
import pandas as pd
from pandas import json_normalize
name = input("Enter name of city: ")#-регістр значення не має - розуміє і в верхньому і в нижньому ,і як завгодно,
#навіть можна українською писати
def search_for_coordinates(name):
    url= f'http://api.openweathermap.org/geo/1.0/direct?q={name}&limit=1&appid={'448c577706d00a044bd20ae8d3fec0e4'}'
    vidpovid = requests.get(url)
    return vidpovid.json()
coord = search_for_coordinates(name)
print(coord)
a = coord[0]
lat = a['lat']
lon = a['lon']
print(a)
print(lat)
print(lon)

def current_weather(lat,lon):

    base_url = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude=minutely,hourly,daily,alerts&units=metric&appid={'448c577706d00a044bd20ae8d3fec0e4'}"

    response = requests.get(base_url)
    return response.json()

weather = current_weather(lat,lon)
# print(weather)
b = weather['current']
a = weather['current']['weather']


c = {**b, **a[0]}

full_table = pd.DataFrame(c)
filter_table = full_table.filter(items=['temp','feels_like','humidity','pressure','wind_speed','wind_deg','description'])
print(filter_table)


