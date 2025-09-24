# Task 2:
# Використовуючи API Нацбанку, вибрати всі доступні курси валют за останні 3 дні (з сьогоднішнім днем, включно),
# з допомогою запитів в розділі '1. Офіційний курс гривні до іноземних валют та облікова ціна банківських металів'.
# Зберегти результати в файлі в форматі JSON, в порядку зростання: код валюти, дата.

import requests
from datetime import datetime, date, timedelta
import json

# Отримуємо дату поточну та 3 дні тому:
today = date.today()
three_days_ago = today - timedelta(days=3)

# Перетворюємо дату на текстовий рядок потрібного формату (YYYYMMDD)
# (з інструкції до сервісу отримання інформації за вибором валюти/металу та діапазоном дат)
today_str = today.strftime("%Y%m%d")                    # Поточна дата
three_days_ago_str = three_days_ago.strftime("%Y%m%d")  # Дата три дні тому

# Отримуємо дані з сайту (в порядку зростання: код валюти r030, дата exchangedate)
url = f"https://bank.gov.ua/NBU_Exchange/exchange_site?start={three_days_ago_str}&end={today_str}&sort=r030&sort=exchangedate&order=asc&json"
response = requests.get(url)

# Якщо дані отримано успішно - зберігаємо в json-файл:
if response.status_code == 200:
    json_response = response.json()
    with open('Exchang.json', 'w', encoding='utf-8') as file:
        json.dump(json_response, file, ensure_ascii=False, indent=4)


