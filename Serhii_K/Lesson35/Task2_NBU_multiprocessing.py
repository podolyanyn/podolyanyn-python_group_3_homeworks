# Task 2:
# Нам потрібно отримати 3 курса валют з API Нацбанку
# (припустимо що API за 1 раз повертає лише курс по одній валюті).
# Спробуємо це зробити синхронно (звичайний підхід), з використанням потоків і з використанням процесів.
# Виміряйте час, для всіх випадків (запустіть по 3 рази, для усереднення результату).

import requests
from datetime import date
import json
import os
import time
import multiprocessing
from concurrent.futures import ThreadPoolExecutor


def NBU_request(val):
    """Функція, що надсилає запит на сайт НБУ, отримує курс валют за певний період часу -
     в нашому випадку поточної доби і зберігає ці дані в форматі json в переданий список list_data,
     також зберігаємо дані в json-файл (це також I/O-bound операція)
     (в запиті також вказується порядок сортування (зростання) за кодом валюти r030)"""

    start_date = date.today().strftime("%Y%m%d")

    url = f"https://bank.gov.ua//NBUStatService/v1/statdirectory/exchange?valcode={val}&date={start_date}&json"
    file_name = 'Exchang_multiprocessing.json'

    # Відправляємо запит на сервер:
    response = requests.get(url)

    # Якщо дані отримано успішно - повертаємо дані у форматі json, а також зберігаємо їх в файл:
    if response.status_code == 200:
        json_response = response.json()

        # Збереження в файл
        save_in_json_file(file_name, json_response)
        return json_response
    else:
        print(f"Помилка {response.status_code} при отриманні даних з сайту")




def save_in_json_file(file_name: str, new_data):
    """Функція, що зберігає дані в файл json"""
    # Спочатку намагаємось прочитати наявні дані з файлу:
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            data = json.load(file)
    except:
        data = []   # Якщо файлу не існує, або він пустий - створюємо новий список даних

    # Додаємо нові дані до списку
    data.append(new_data)

    # Записуємо оновлений список назад у файл
    try:
        with open(file_name, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Помилка при збереженні даних: [{e}]")



if __name__ == '__main__':
    # Потрібен список валют, по яких потрібно зробити запити:
    list_val = ['usd', 'eur', 'gbp']

    # Попереднє видалення файлу:
    if os.path.exists('Exchang_multiprocessing.json'):
        os.remove('Exchang_multiprocessing.json')

    # Варіант 1 - без створення потоків. Просто запити в циклі
    results = []

    start_time = time.perf_counter()

    for val in list_val:
        results.append(NBU_request(val))

    duration2 = time.perf_counter() - start_time

    print(f"Отримання і збереження даних (без використання потоків) за {duration2} сек.")   # 2.7806955999694765 сек.


    # Попереднє видалення файлу:
    if os.path.exists('Exchang_multiprocessing.json'):
        os.remove('Exchang_multiprocessing.json')


    # Варіант 2 - з потоками.
    results = []
    list_threads = []

    start_time2 = time.perf_counter()

    with ThreadPoolExecutor() as executor:
        results = list(executor.map(NBU_request, list_val))

    duration1 = time.perf_counter() - start_time2

    print(f"Отримання і збереження даних (з використанням потоків) за {duration1} сек.")    # 1.2195232999511063 сек.


    # Попереднє видалення файлу:
    if os.path.exists('Exchang_multiprocessing.json'):
        os.remove('Exchang_multiprocessing.json')


    # 3 Варіант. Мультіпроцессінг
    results = []

    start_time1 = time.perf_counter()

    with multiprocessing.Pool() as pool:
        results = pool.map(NBU_request, list_val)

    duration1 = time.perf_counter() - start_time1

    print(f"Отримання і збереження даних (з використанням процесів) за {duration1} сек.")   # 1.8159647000138648 сек.

    # Це - приклад I/O-bound задач, і тут використання потоків дало найбільшу продуктивність (1.2 сек),
    # в порівнянні з використанням мультипроцессінгу (1.8 сек) і з використанням синхронних обчислень (2.7 сек).