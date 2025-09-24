# Task 3:
# Використовуючи API Нацбанку, вибрати всі доступні курси валют за останні 3 дні (з сьогоднішнім днем, включно),
# з допомогою запитів в розділі '1. Офіційний курс гривні до іноземних валют та облікова ціна банківських металів'.
# Зберегти результати в файлі в форматі JSON, в порядку зростання: код валюти, дата.
# При реалізації задачі використати різні потоки.

import requests
from datetime import date, timedelta
import json
import threading
import time


def NBU_request(start_date: date, end_date: date, list_data: list):
    """Функція, що надсилає запит на сайт НБУ, отримує курс валют за певний період часу -
     в нашому від попередньої доби до поточної доби і зберігає ці дані в форматі json в переданий список list_data
     (в запиті також вказується порядок сортування (зростання) за кодом валюти r030)"""

    # Рядок запиту:
    url = f"https://bank.gov.ua/NBU_Exchange/exchange_site?start={start_date}&end={end_date}&sort=r030&order=asc&json"

    response = requests.get(url)

    # Якщо дані отримано успішно - повертаємо дані у форматі json:
    if response.status_code == 200:
        json_response = response.json()
        list_data.append(json_response)
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
    # Так як потрібно отримати дані за кілька днів з використанням потоків,
    # то розділяти потоки будемо по дням (кожен запит на сайт буде обробляти свій період часу - добу)

    # Кількість днів за умовами задачі (останні 3 дні), за які потрібно зібрати дати, починаючи від поточної
    delta_days = 3

    # Потрібен список дат, по яких потрібно зробити запити:
    list_dates = []

    # Поточна дата:
    today = date.today()

    # Всього потрібно мати на одну дату більше ніж задана кількість днів (сьогодні-вчора; вчора-позавчора; позавчора-позапозавчора,...)
    # Для забезпечення сортування результатів в порядку зростання дат потрібно щоб дати в списку були в зворотньому порядку - від старішої до поточної
    # Для того, щоб дати йшли в зворотньому порядку - розраховуємо дати в циклі від delta_days до -1 з шагом -1:
    for i in range(delta_days, -1, -1):
        new_date = today - timedelta(days=i)
        # Перетворюємо дату на текстовий рядок потрібного формату (YYYYMMDD)
        new_date = new_date.strftime("%Y%m%d")
        # Зберігаємо дати в список
        list_dates.append(new_date)

    # Для багатопотокового запиту потрібно створити
    # список для збереження результатів запитів,
    # та список thread для роботи з потоками:
    list_data = []
    list_threads = []


    # Для наочності підраховуємо кількість затраченого часу
    start_time1 = time.perf_counter()

    # Для запиту на сайт під кожну пару дат в списку list_dates створюємо свій потік.
    for i in range(len(list_dates) - 1):
        t = threading.Thread(target=NBU_request, args=(list_dates[i + 1], list_dates[i], list_data))
        list_threads.append(t)
        t.start()

    # Очікуємо на завершення роботи всіх потоків:
    for t in list_threads:
        t.join()

    # Збереження всіх отриманих даних в файл:
    file_name = 'Exchang.json'
    for data in list_data:
            save_in_json_file(file_name, data)

    # Затрачений час:
    duration1 = time.perf_counter() - start_time1
    print(f"Отримання і збереження даних (з використанням потоків) за {duration1} сек.")