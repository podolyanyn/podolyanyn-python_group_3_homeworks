# Task 2:
# Нам потрібно отримати 3 курса валют з API Нацбанку
# (припустимо що API за 1 раз повертає лише курс по одній валюті).
# Спробуємо це зробити асінхронно.

from datetime import date
import json
import time
import asyncio
import aiohttp
import os


async def NBU_request(val):
    """Функція, що надсилає запит на сайт НБУ, отримує курс валют за певний період часу -
     в нашому випадку поточної доби і повертає ці дані в форматі json,
     також зберігаємо дані в json-файл (це також I/O-bound операція)"""

    start_date = date.today().strftime("%Y%m%d")

    url = f"https://bank.gov.ua//NBUStatService/v1/statdirectory/exchange?valcode={val}&date={start_date}&json"
    file_name = 'Exchang_async.json'

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                json_response = await response.json()

                await save_in_json_file(file_name, json_response)
                return json_response
            else:
                print(f"Помилка {response.status} при отриманні даних з сайту")


async def save_in_json_file(file_name: str, new_data):
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



async def main():
    # Потрібен список валют, по яких потрібно зробити запити:
    list_val = ['usd', 'eur', 'gbp']

    # Список для зберігання результатів запитів
    results = []
    tasks = []

    # Попереднє видалення файлу:
    if os.path.exists('Exchang_async.json'):
        os.remove('Exchang_async.json')

    start_time = time.perf_counter()

    for val in list_val:
        tasks.append(asyncio.create_task(NBU_request(val)))
    results = await asyncio.gather(*tasks)

    duration1 = time.perf_counter() - start_time

    print(results)
    print(f"Отримання і збереження даних (асінхронний метод) за {duration1} сек.")   # 0.10446699999738485 сек.


if __name__ == '__main__':
    asyncio.run(main())