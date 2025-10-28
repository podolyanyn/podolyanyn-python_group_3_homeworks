import requests
import time
from datetime import date
from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Pool

currency_list = ['USD', 'EUR', 'GBP']


def get_rate(currency):

    today = date.today().strftime("%Y%m%d")
    url = f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode={currency}&date={today}&json"

    response = requests.get(url)
    if response.ok:
        data = response.json()
        return data[0]['rate'] if data else 0
    else:
        print(f"Error for {currency}: {response.status_code}")
        return 0


if __name__ == "__main__":
    def sync_get():
        start = time.time()
        rates = []
        for i in currency_list:
            rates.append(get_rate(i))
        return time.time() - start

    def thread_get():
        start = time.time()
        with ThreadPoolExecutor(max_workers=3) as executor:
            rates = list(executor.map(get_rate, currency_list))
        return time.time() - start

    def proc_get():
        start = time.time()
        with Pool(processes=3) as pool:
            rates = pool.map(get_rate, currency_list)
        return time.time() - start


    print("Sync (5 times)")
    sync_times = [sync_get() for i in range(5)]
    avg_sync = sum(sync_times) / len(sync_times)
    print("Times:", [f"{t:.2f}s" for t in sync_times])
    print(f"Average time: {avg_sync:.2f}s\n")

    print("Thread (5 times)")
    thread_times = [thread_get() for i in range(5)]
    avg_thread = sum(thread_times) / len(thread_times)
    print("Times:", [f"{t:.2f}s" for t in thread_times])
    print(f"Average time: {avg_thread:.2f}s\n")

    print("Proc (5 times)")
    proc_times = [proc_get() for i in range(5)]
    avg_proc = sum(proc_times) / len(proc_times)
    print("Times:", [f"{t:.2f}s" for t in proc_times])
    print(f"Average time: {avg_proc:.2f}s\n")

