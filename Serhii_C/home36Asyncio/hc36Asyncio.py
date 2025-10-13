# Завдання 1
#
# Практика асинхронного коду
# Створіть окремий асинхронний код для обчислення чисел Фібоначчі, факторіала, квадратів та кубічних чисел
# для вхідного числа. Заплануйте виконання цього коду за допомогою asyncio.gather для списку цілих чисел
# від 1 до 10. Вам потрібно отримати чотири списки результатів від відповідних функцій.
# Перепишіть код, щоб використовувати прості функції для отримання тих самих результатів,
# але з використанням багатопроцесорної бібліотеки. Зафіксуйте час виконання обох реалізацій,
# дослідіть результати, яка реалізація є ефективнішою, чому ви отримали такий результат.
# import random
# import asyncio
# import time
#
# from pyparsing import results
# NUMBERS = [random.randint(0, 10) for i in range(10)]
#
#
#
# async def fibonacci(n):
#
#     if not isinstance(n, int) or n < 0:
#         raise ValueError("Число має бути невід'ємним цілим числом.")
#
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#
#
#     a, b = 0, 1
#     for _ in range(2, n + 1):
#         a, b = b, a + b
#
#     return b
#
#
# async def factorial(n: int) -> int:
#
#
#     if not isinstance(n, int) or n < 0:
#         raise ValueError("Число має бути невід'ємним цілим числом.")
#
#     if n == 0:
#         return 1
#
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#
#     return result
#
#
#
# async def square(n: int | float) -> int | float:
#
#     return n ** 2
#
#
#
# async def cube(n: int | float) -> int | float:
#
#     return n ** 3
#
# async def main():
#     start_time = time.perf_counter()
#
#
#     tasks1 = []
#     tasks2 = []
#     tasks3 = []
#     tasks4 = []
#
#     for n in NUMBERS:
#         tasks1.append(asyncio.create_task(fibonacci(n)))
#         tasks2.append(asyncio.create_task(factorial(n)))
#         tasks3.append(asyncio.create_task(square(n)))
#         tasks4.append(asyncio.create_task(cube(n)))
#     all_tasks = tasks1 + tasks2 + tasks3 + tasks4
#     results = await asyncio.gather(*all_tasks)
#     fib_results = results[0:10]
#     fact_results = results[10:20]
#     square_results = results[20:30]
#     cube_results = results[30:40]
#     print(f'Фібоначі :{fib_results}')
#     print(f'Factorial: {fact_results}')
#     print(f'Square :{square_results}')
#     print(f'Cube : {cube_results}')
#     duration1 = time.perf_counter() - start_time
#     print(f" (асінхронний метод) за {duration1} сек.")
#
# if __name__ == '__main__':
#     asyncio.run(main())     # Асінхронний метод
#
# from concurrent.futures import ProcessPoolExecutor
#
#
# def fibonacci(n):
#
#     if not isinstance(n, int) or n < 0:
#         raise ValueError("Число має бути невід'ємним цілим числом.")
#
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#
#
#     a, b = 0, 1
#     for _ in range(2, n + 1):
#         a, b = b, a + b
#
#     return b
#
#
# def factorial(n: int) -> int:
#
#
#     if not isinstance(n, int) or n < 0:
#         raise ValueError("Число має бути невід'ємним цілим числом.")
#
#     if n == 0:
#         return 1
#
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#
#     return result
#
#
#
# def square(n: int | float) -> int | float:
#
#     return n ** 2
#
#
#
# def cube(n: int | float) -> int | float:
#
#     return n ** 3
#
# if __name__=='__main__':
#     start_time = time.perf_counter()
#
#     with ProcessPoolExecutor(max_workers=4) as executor:
#         results_fib = list(executor.map(fibonacci, NUMBERS))
#         results_fact = list(executor.map(factorial, NUMBERS))
#         results_square = list(executor.map(square, NUMBERS))
#         results_cube = list(executor.map(cube, NUMBERS))
#
#         print(f"Результати фібоначчі: {results_fib}")
#         print(f"Факторіал: {results_fact}")
#         print(f"Квадрати: {results_square}")
#         print(f"Куби: {results_cube}")
#     end_time = time.perf_counter()
#     print(f'Процессорний екзекютор метод executor.map :{end_time - start_time}')

# Завдання 3
# Echo-сервер з asyncio
# Створіть socket echo-сервер, який обробляє кожне підключення за допомогою завдань asyncio.


# import requests
# import threading
# import pickle
# import multiprocessing
# import socket
#
# def get_currency_info(start_date, end_date, currency,connection):
#
#
#     response = requests.get(f'https://bank.gov.ua/NBU_Exchange/exchange_site?start={start_date}&end={end_date}&valcode={currency}&sort=exchangedate&order=desc&json')
#     if response.status_code == 200:
#         print(f'Дані по {currency} отримано')
#         # print(response.json())
#     for_sending = []
#     for element in response.json():
#         currency_name = element['enname']
#         day = element['exchangedate']
#         rate = element['rate']
#         for_sending.append((currency_name,day, rate))
#     # print(for_sending)
#     data_for_sending = pickle.dumps(for_sending)
#     connection.sendall(data_for_sending)
#     print(f'Данні по {currency} відправлені')
#     connection.close()
#
# def obgortka(connection: socket.socket, client_address):
#     data = connection.recv(1024)
#     received_tuple = pickle.loads(data)
#     start_date, end_date, currency = received_tuple
#     get_currency_info(start_date, end_date, currency,connection)
#
# import asyncio
# import pickle
#
#
#
# async def main(sock):
#
#     while True:
#
#         print ('waiting for a connection')
#         connection, client_address = await asyncio.to_thread(sock.accept)
#         print(f'З\'єднання з : {client_address}')
#         task = asyncio.create_task(asyncio.to_thread(obgortka, connection, client_address))
#
#
# if __name__ == '__main__':
#     sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     server_address = ('localhost', 8085)
#
#     sock.bind(server_address)
#     sock.listen(5)
#     asyncio.run(main(sock))

#варіант 2 ---      З допомогою ШІ

# import aiohttp
# import asyncio
# import pickle
# import json
#
# from typing import Tuple, List, Dict, Any
#
#
# async def get_currency_info(start_date, end_date, currency):
#     url = f'https://bank.gov.ua/NBU_Exchange/exchange_site?start={start_date}&end={end_date}&valcode={currency}&sort=exchangedate&order=desc&json'
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url) as response:
#             if response.status == 200:
#                 print(f'Дані по {currency} отримано')
#                 json_response = await response.text()
#                 json_response = json.loads(json_response)
#
#                 for_sending = []
#                 for element in json_response:
#                     currency_name = element['enname']
#                     day = element['exchangedate']
#                     rate = element['rate']
#                     for_sending.append((currency_name,day, rate))
#
#     return for_sending
#
# async def handle_client(reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
#
#     client_address = writer.get_extra_info('peername')
#     print(f"З'єднання прийнято від: {client_address}")
#     data = await reader.read(1024)
#     received_tuple: Tuple[str, str, str] = pickle.loads(data)
#     start_date, end_date, currency = received_tuple
#     processed_data = await get_currency_info(start_date, end_date, currency)
#     data_for_sending = pickle.dumps(processed_data)
#     writer.write(data_for_sending)
#     await writer.drain()
#     print(f"Дані по {currency} відправлені")
#     writer.close()
#     await writer.wait_closed()
#
# async def start_async_server(host: str, port: int):
#     print('Waiting for connection...')
#     server = await asyncio.start_server(handle_client, host, port)
#     addr = server.sockets[0].getsockname()
#     async with server:
#         await server.serve_forever()
#
#
# if __name__ == '__main__':
#     HOST = 'localhost'
#     PORT = 8085
#
#
#     try:
#         asyncio.run(start_async_server(HOST, PORT))
#     except KeyboardInterrupt:
#         print("\nСервер зупинено користувачем.")

# Завдання 2
#
# Запити за допомогою asyncio та aiohttp
# Завантажте всі коментарі з вибраного вами subreddit за допомогою URL-адреси:
# https://api.pushshift.io/reddit/comment/search/ .
# В результаті збережіть усі коментарі в хронологічному порядку у форматі JSON та виведіть їх у файл.
# Для цього завдання використовуйте бібліотеки asyncio та aiohttp для здійснення запитів до API Reddit.

# import asyncio
# import aiohttp
# import time
# import json
# from typing import List, Dict, Any, Tuple
#
#
# # --- 1. Асинхронна функція для отримання даних ---
#
# async def fetch_nbu_data_async(start_date: str, end_date: str) -> Tuple[List[Dict[str, Any]], float]:
#
#     base_url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/grossextdebt"
#
#     params = {
#         'startdate': start_date,
#         'enddate': end_date,
#         'json': ''
#     }
#
#     start_time = time.perf_counter()
#
#
#     async with aiohttp.ClientSession() as session:
#
#         async with session.get(base_url, params=params) as response:
#             if response.status != 200:
#                 print(f"Помилка HTTP: {response.status} для {start_date}")
#                 return [], 0.0
#
#
#             data = await response.text()
#             data = json.loads(data)
#
#
#     end_time = time.perf_counter()
#     duration = end_time - start_time
#
#
#     return data, duration
#
#
#
#
# async def main_async_fetch():
#
#     periods = [
#         ("20160101", "20160630"),
#         ("20170101", "20170630"),
#         ("20180101", "20180630"),
#         ("20190101", "20190630"),
#     ]
#
#     overall_start_time = time.perf_counter()
#
#
#     tasks = []
#     for start, end in periods:
#
#         tasks.append(fetch_nbu_data_async(start, end))
#
#
#     results: List[Tuple[List[Dict[str, Any]], float]] = await asyncio.gather(*tasks)
#     print(results)
#
#     overall_end_time = time.perf_counter()
#     total_time = overall_end_time - overall_start_time
#     with open("data36_for.json", "w", encoding="utf-8") as f:
#         json.dump(results, f, ensure_ascii=False, indent=4)
#     print(total_time)
#
#
#
#
# if __name__ == '__main__':
#     asyncio.run(main_async_fetch())
