import requests
import json
#-------------------------------------------------------- 2 ------------------------------------------------------------
"""виконати наступну задачу:
       Використовуючи API Нацбанку, вибрати всі доступні курси валют за останні 3 дні (з сьогоднішнім днем, включно), з допомогою запитів в розділі '1. Офіційний курс гривні до іноземних валют та облікова ціна
       банківських металів'.
       Зберегти результати в файлі в форматі JSON, в порядку зростання: код валюти, дата."""

response = requests.get('https://bank.gov.ua/NBU_Exchange/exchange_site?start=20250920&end=20250923&sort=exchangedate&order=asc&json')

with open(f'{input('Pls enter a name for new file with currencies: ')}.json', 'w', encoding='utf-8') as fo:
    json.dump(response.json(), fo, ensure_ascii=False, indent=4)
