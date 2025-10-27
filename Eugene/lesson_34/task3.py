import json
import time
from datetime import date, timedelta
from threading import Thread, Lock
import requests


URL = "https://bank.gov.ua/NBU_Exchange/exchange_site?start={d}&end={d}&sort=r030&order=asc&json"


def exchange_request(day: str, data, lock: Lock):

    print(f"Request per day {day}")

    try:

        response = requests.get(URL.format(d=day))
        response.raise_for_status()

        rates = response.json()

        with lock:
            data.extend(rates)

        print(f"Received {len(rates)} records for {day}")

    except requests.RequestException as e:
        print(f"Request error for {day}: {e}")


def main() -> None:

    today = date.today()
    dates = []

    for i in range(2, -1, -1):
        day_date = today - timedelta(days=i)
        dates.append(day_date.strftime("%Y%m%d"))

    print(f"Collect data for dates: {dates}")

    all_data = []
    data_lock = Lock()

    start_time = time.perf_counter()

    threads = []
    for day in dates:
        thread = Thread(target=exchange_request, args=(day, all_data, data_lock))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    if not all_data:
        print("No data. Check the API or the Internet.")
        return

    all_data.sort(key=lambda rate: (rate["r030"], rate["exchangedate"]))

    filename = "exchange.json"
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(all_data, file, ensure_ascii=False, indent=2)

    duration = time.perf_counter() - start_time
    print(f"Data for {len(dates)} days saved in {filename} for {duration:.2f} seconds.")
    print(f"Total records: {len(all_data)}")


if __name__ == "__main__":
    main()
