#====================================================== 1 with AI help ==============================================================
"""Task 1

Primes

NUMBERS = [
   2,  # prime
   1099726899285419,
   1570341764013157,  # prime
   1637027521802551,  # prime
   1880450821379411,  # prime
   1893530391196711,  # prime
   2447109360961063,  # prime
   3,  # prime
   2772290760589219,  # prime
   3033700317376073,  # prime
   4350190374376723,
   4350190491008389,  # prime
   4350190491008390,
   4350222956688319,
   2447120421950803,
   5,  # prime
]
We have the following input list of numbers, some of them are prime. You need to create a utility function that takes as input a number and returns a bool, whether it is prime or not.



Use ThreadPoolExecutor and ProcessPoolExecutor to create different concurrent implementations for filtering NUMBERS.

Compare the results and performance of each of them."""
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

NUMBERS = [
    2, 1099726899285419, 1570341764013157, 1637027521802551,
    1880450821379411, 1893530391196711, 2447109360961063, 3,
    2772290760589219, 3033700317376073, 4350190374376723,
    4350190491008389, 4350190491008390, 4350222956688319,
    2447120421950803, 5
]

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def find_primes_threadpool(numbers):
    start = time.perf_counter()
    with ThreadPoolExecutor() as executor:
        results = list(executor.map(is_prime, numbers))
    end = time.perf_counter()
    primes = [n for n, is_p in zip(numbers, results) if is_p]
    print(f"ThreadPoolExecutor: {end - start:.2f} sec")
    return primes


def find_primes_processpool(numbers):
    start = time.perf_counter()
    with ProcessPoolExecutor() as executor:
        results = list(executor.map(is_prime, numbers))
    end = time.perf_counter()
    primes = [n for n, is_p in zip(numbers, results) if is_p]
    print(f"ProcessPoolExecutor: {end - start:.2f} sec")
    return primes


if __name__ == "__main__":
    primes_thread = find_primes_threadpool(NUMBERS)
    primes_process = find_primes_processpool(NUMBERS)

    print("\nThreadPoolExecutor primes:", primes_thread)
    print("ProcessPoolExecutor primes:", primes_process)



#====================================================== 2 ==============================================================
"""Requests using concurrent and multiprocessing libraries

Download all comments from a subreddit of your choice using URL: https://api.pushshift.io/reddit/comment/search/ .

As a result, store all comments in chronological order in JSON and dump it to a file.
For this task use concurrent and multiprocessing libraries for making requests to Reddit API."""
# import requests
# import multiprocessing
# import json
#
#
#
# def get_currency_info(start_date, end_date, currency):
#
#     response = requests.get(f'https://bank.gov.ua/NBU_Exchange/exchange_site?start={start_date}&end={end_date}&valcode={currency}&sort=exchangedate&order=asc&json')
#     data = response.json()
#
#     with open(f'{currency}.json', 'w', encoding='utf-8') as fo:
#         json.dump(response.json(), fo, indent=4, ensure_ascii=False)
#
# if __name__ == '__main__':
#     currencies_list = ['eur', 'usd', 'gbp']
#     processes_list = []
#
#     for currency in currencies_list:
#         p = multiprocessing.Process(target=get_currency_info, args=('20251004', '20251007', currency))
#         processes_list.append(p)
#         p.start()
#
#     for p in processes_list:
#         p.join()
#
#     print("------>All files were created")

#====================================================== 3 ==============================================================
"""Echo server with multiprocessing

Create a socket echo server that handles each connection using the multiprocessing library."""

# import socket
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
# def handle_connection(connection, client_address):
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
# def main():
#     HOST = 'localhost'
#     PORT = 8890
#
#     server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     server_address = (HOST, PORT)
#     print('starting up --- TCP SERVER --- on {} port {}'.format(*server_address))
#     server.bind(server_address)
#
#     server.listen(5)
#     processes_list = []
#
#     while True:
#         # Wait for a connection
#         print('waiting for a connection')
#         connection, client_address = server.accept()
#         p = multiprocessing.Process(target=handle_connection, args=(connection, client_address), daemon=True)
#         processes_list.append(p)
#         p.start()
#
# if __name__ == "__main__":
#     multiprocessing.freeze_support()  # важливо для Windows
#     main()