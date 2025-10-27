import requests
from datetime import date, timedelta
import json

end = date.today()
start = end - timedelta(days=2)

end_str = end.strftime("%Y%m%d")
start_str = start.strftime("%Y%m%d")

url = f"https://bank.gov.ua/NBU_Exchange/exchange_site?start={start_str}&end={end_str}&sort=r030&sort=exchangedate&order=asc&json"
response = requests.get(url)

if response.ok:
    data = response.json()

    data.sort(key=lambda x: (x['r030'], x['exchangedate']))

    with open('exchange.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

else:
    print(f'Error:', response.status_code)