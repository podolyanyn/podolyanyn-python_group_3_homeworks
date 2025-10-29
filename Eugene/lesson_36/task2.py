import asyncio
import aiohttp
from datetime import date
import time


currency_list = ['USD', 'EUR', 'GBP']


async def get_rate(session, currency):
    today_date = date.today().strftime("%Y%m%d")
    url = f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode={currency}&date={today_date}&json"

    async with session.get(url) as resp:
        if resp.ok:
            data = await resp.json()
            return data[0]['rate'] if data else 0
        print(f"Error for {currency}: {resp.status}")
        return 0


async def main_async():
    start = time.time()
    async with aiohttp.ClientSession() as session:
        tasks = [get_rate(session, curr) for curr in currency_list]
        rates = await asyncio.gather(*tasks)
    end = time.time()
    print(f"Async time: {end - start:.2f} сек.")
    print(f"Currency: {currency_list}: {rates}")

if __name__ == "__main__":
    asyncio.run(main_async())