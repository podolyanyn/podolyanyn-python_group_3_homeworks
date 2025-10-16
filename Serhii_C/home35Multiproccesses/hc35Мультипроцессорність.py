# Завдання 2
# Запити з використанням бібліотек паралельної та багатопроцесорної обробки
# Завантажте всі коментарі з вибраного вами subreddit за допомогою URL-адреси:
# https://api.pushshift.io/reddit/comment/search/ .
# В результаті збережіть усі коментарі в хронологічному порядку у форматі JSON та виведіть їх у файл.
# Для цього завдання використовуйте бібліотеки паралельної та багатопроцесорної обробки для здійснення запитів до API Reddit.
#Багатопоточний метод беру з попередньої домашки.

# import requests
# import json
# import threading
# import time
# import multiprocessing
#
# def fetch_nbu_data(start,end):
#     """Отримання даних з API НБУ"""
#     base_url = f"https://bank.gov.ua/NBUStatService/v1/statdirectory/grossextdebt?{start}=20160301&{end}=20170601&json"
#
#     response = requests.get(base_url)
#     # print(response.json())
#
#
#
#     with open("data2_for.json", "w", encoding="utf-8") as f:
#         json.dump(response.json(), f, ensure_ascii=False, indent=4)
# start_time = time.perf_counter()
# t = threading.Thread(target=fetch_nbu_data, args=(20160301,20170601))
# t.start()
# t.join()
# end_time = time.perf_counter()
# print(f'Потоковий  підхід :{end_time - start_time}')

#############Multiprocessing

# if __name__=='__main__':
#     start_time = time.perf_counter()
#     process = multiprocessing.Process(target=fetch_nbu_data, args=(20160301,20170601))
#     process.start()
#     process.join()
#     end_time = time.perf_counter()
#     print(f'Мультипроцессорний   підхід :{end_time - start_time}')

# В данному простому зав'данні потоки працюють краще , адже багато часу витрачається саме на побудову потоку.


# Завдання 3
#
# Echo-сервер з багатопроцесорною обробкою
# Створіть socket echo-сервер, який обробляє кожне з('єднання, використовуючи бібліотеку багатопроцесорної '
# 'обробки.)

import requests
import threading
import pickle
import multiprocessing

def get_currency_info(start_date, end_date, currency,connection):


    response = requests.get(f'https://bank.gov.ua/NBU_Exchange/exchange_site?start={start_date}&end={end_date}&valcode={currency}&sort=exchangedate&order=desc&json')
    if response.status_code == 200:
        print(f'Дані по {currency} отримано')
        # print(response.json())
    for_sending = []
    for element in response.json():
        currency_name = element['enname']
        day = element['exchangedate']
        rate = element['rate']
        for_sending.append((currency_name,day, rate))
    # print(for_sending)
    data_for_sending = pickle.dumps(for_sending)
    connection.sendall(data_for_sending)
    print(f'Данні по {currency} відправлені')
    connection.close()





import pickle
import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 8084)
if __name__=='__main__':
    print ('start with {} port{}'.format(*server_address))
    sock.bind(server_address)
    sock.listen(5)

    while True:
        print ('waiting for a connection')
        connection, client_address = sock.accept()
        print('connection from', client_address)
        data = connection.recv(1024)
        received_tuple = pickle.loads(data)
        start_date, end_date, currency = received_tuple
        t = multiprocessing.Process(target=get_currency_info, args=(start_date, end_date, currency,connection))
        t.start()
        connection.close()
        print (f'Процесс для {currency} почався')

# Завдання 1
#
# Прості числа
#
# ЧИСЛА = [
# 2, # просте число
# 1099726899285419,
# 1570341764013157, # просте число
# 1637027521802551, # просте число
# 1880450821379411, # просте число
# 1893530391196711, # просте число
# 2447109360961063, # просте число
# 3, # просте число
# 2772290760589219, # просте число
# 3033700317376073, # просте число
# 4350190374376723,
# 4350190491008389, # просте число
# 4350190491008390,
# 4350222956688319,
# 2447120421950803,
# 5, # просто
# ]
# У нас є наступний вхідний список чисел, деякі з яких є простими. Вам потрібно створити допоміжну функцію ,
#  яка приймає на вхід число та повертає логічне значення, незалежно від того, просте воно чи ні.
# Використовуйте ThreadPoolExecutor та ProcessPoolExecutor для створення різних одночасних реалізацій фільтрації ЧИСЕЛ.
# Порівняйте результати та продуктивність кожної з них.

import math
from typing import Tuple


def is_prime(number):

    if number <= 1:
        return (number, False)


    if number == 2:
        return (number, True)


    if number % 2 == 0:
        return (number, False)


    max_divisor = int(math.sqrt(number))


    for i in range(3, max_divisor + 1, 2):
        if number % i == 0:

            return (number, False)


    return (number, True)


from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor
import time

NUMBERS = [
   2,
   1099726899285419,
   1570341764013157,
   1637027521802551,
   1880450821379411,
   1893530391196711,
   2447109360961063,
   3,
   2772290760589219,
   3033700317376073,
   4350190374376723,
   4350190491008389,
   4350190491008390,
   4350222956688319,
   2447120421950803,
   5,
]
# start_time = time.perf_counter()
# with ThreadPoolExecutor(max_workers=3) as executor:
#     results_iterator = executor.map(is_prime, NUMBERS)
#     results = list(results_iterator)
#
#     print(f"Результати: {results}")
# end_time = time.perf_counter()
# print(f'Потоковий екзекютор метод executor.map :{end_time - start_time}')#- 26.04279089999909 сек
if __name__=='__main__':
    start_time = time.perf_counter()
    with ProcessPoolExecutor(max_workers=4) as executor:
        results_iterator = executor.map(is_prime, NUMBERS)
        results = list(results_iterator)
        print(f"Результати: {results}")
    end_time = time.perf_counter()
    print(f'Процессорний екзекютор метод executor.map :{end_time - start_time}')#-9.474761800000124 сек