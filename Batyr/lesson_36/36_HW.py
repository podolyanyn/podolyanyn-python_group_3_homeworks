#=========================================================== 1 AI help =========================================================
"""Task 1

Practice asynchronous code

Create a separate asynchronous code to calculate Fibonacci, factorial, squares and cubic for an input number. Schedule the execution of this code using asyncio.gather for a list of integers from 1 to 10. You need to get four lists of results from corresponding functions.

Rewrite the code to use simple functions to get the same results but using a multiprocessing library. Time the execution of both realizations, explore the results, what realization is more effective, why did you get a result like this."""
import asyncio, multiprocessing
import time
import math

async def fibonacci(n):
    if n <= 1:
        return n
    return await fibonacci(n - 1) + await fibonacci(n - 2)

async def factorial(n):
    return math.factorial(n)

async def square(n):
    return n * n

async def cubic(n):
    return n ** 3


async def main_async():
    nums = list(range(1, 30))

    start = time.perf_counter()
    fib_results, fact_results, square_results, cubic_results = await asyncio.gather(
        asyncio.gather(*(fibonacci(n) for n in nums)),
        asyncio.gather(*(factorial(n) for n in nums)),
        asyncio.gather(*(square(n) for n in nums)),
        asyncio.gather(*(cubic(n) for n in nums)),
    )
    end = time.perf_counter()

    print(f"AsyncIO Time: {end - start:.4f} seconds")
    print("Fibonacci:", fib_results)
    print("Factorial:", fact_results)
    print("Squares:", square_results)
    print("Cubes:", cubic_results)
asyncio.run(main_async())


# def fibonacci(n):
#     if n <= 1:
#         return n
#     return fibonacci(n - 1) + fibonacci(n - 2)
#
# def factorial(n):
#     return math.factorial(n)
#
# def square(n):
#     return n * n
#
# def cubic(n):
#     return n ** 3
#
# def main_multiprocessing():
#     nums = list(range(1, 30))
#     start = time.perf_counter()
#     with multiprocessing.Pool() as pool:
#         fib_results = pool.map(fibonacci, nums)
#         fact_results = pool.map(factorial, nums)
#         square_results = pool.map(square, nums)
#         cubic_results = pool.map(cubic, nums)
#     end = time.perf_counter()
#
#     print(f"Multiprocessing Time: {end - start:.4f} seconds")
#     print("Fibonacci:", fib_results)
#     print("Factorial:", fact_results)
#     print("Squares:", square_results)
#     print("Cubes:", cubic_results)
#
# if __name__ == "__main__":
#     main_multiprocessing()



#=========================================================== 2 =========================================================
"""Task 2

Requests using asyncio and aiohttp"""

# import asyncio, aiohttp
# import json
#
# async def get_currency_info(session, start_date, end_date, currency):
#     url = f'https://bank.gov.ua/NBU_Exchange/exchange_site?start={start_date}&end={end_date}&valcode={currency}&sort=exchangedate&order=asc&json'
#     async with session.get(url) as response:
#         data = await response.json()
#         with open(f'{currency}.json', 'w', encoding='utf-8') as fo:
#             json.dump(data, fo, indent=4, ensure_ascii=False)
#         return data
#
# async def main():
#     currencies_list = ['eur', 'usd', 'gbp']
#     start_date, end_date = '20251004', '20251007'
#
#     tasks = []
#     async with aiohttp.ClientSession() as session:
#         for currency in currencies_list:
#             tasks.append(get_currency_info(session, start_date, end_date, currency))
#
#         await asyncio.gather(*tasks)
#
# asyncio.run(main())

#=========================================================== 3 AI help=========================================================
"""Task 3

Echo server with asyncio

Create a socket echo server which handles each connection using asyncio Tasks."""

# import socket
# import asyncio
#
# import multiprocessing
#
# def encode_with_ceasar(in_str, code=0):
#     result = ''
#     code = code % 26
#
#     for letter in in_str:
#         letter_code = ord(letter)
#
#         if letter_code < 65 or (90 < letter_code < 97) or (letter_code > 122):
#             result += letter
#             continue
#         new_code = letter_code + code
#
#         if code >= 0:
#             if 65 <= letter_code <= 90 < new_code:
#                 codes_difference = (new_code - 90) % 26
#                 new_code = 64 + codes_difference
#
#             if 97 <= letter_code <= 122 < new_code:
#                 codes_difference = (new_code - 122) % 26
#                 new_code = 96 + codes_difference
#
#         else:
#             if new_code < 65 <= letter_code <= 90:
#                 codes_difference = abs(65 - new_code) % 26
#
#                 new_code = 91 - codes_difference
#
#             if new_code < 97 <= letter_code <= 122:
#                 codes_difference = abs(97 - new_code) % 26
#                 new_code = 123 - codes_difference
#         result += chr(new_code)
#     return result
#
# async def handle_connection(connection, client_address):
#     with connection:
#         print('Connected by', client_address)
#         while True:
#             data = connection.recv(1024)
#
#             if not data:
#                 break
#             values = data.decode().split('&')
#             print(values)
#             result = encode_with_ceasar(encode_with_ceasar(values[0], int(values[1])))
#             print(result)
#
#             connection.sendall(result.encode())
#
# async def main():
#     HOST = 'localhost'
#     PORT = 8890
#
#     server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     server_address = (HOST, PORT)
#     print('starting up --- TCP SERVER --- on {} port {}'.format(*server_address))
#     server.bind(server_address)
#
#     server.listen(5)
#
#     while True:
#         # Wait for a connection
#         print('waiting for a connection')
#         connection, client_address = server.accept()
#
#         task = asyncio.create_task(handle_connection(connection, client_address))
#         await task
#
# asyncio.run(main())