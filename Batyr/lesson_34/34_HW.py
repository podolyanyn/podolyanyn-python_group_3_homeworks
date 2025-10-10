#=========================================================== 1 =========================================================
"""Task 1

A shared counter

Make a class called Counter, and make it a subclass of the Thread class in the Threading module. Make the class have two
 global variables, one called counter set to 0, and another called rounds set to 100.000. Now implement the run() method,
  let it include a simple for-loop that iterates through rounds (e.i. 100.000 times) and for each time increments
   the value of the counter by 1. Create 2 instances of the thread and start them, then join them and check the result of
    the counter, it should be 200.000, right? Run it a couple of times and consider some different reasons why you get the
     answer that you get."""

# from threading import Thread
#
#
# class Counter(Thread):
#     counter = 0
#     rounds = 100000
#
#     def run(self):
#         for i in range(self.rounds):
#             self.counter += 1
#         return self.counter
#
# counter_1 = Counter()
# counter_2 = Counter()
# counter_1.start()
# counter_2.start()
# counter_1.join()
# counter_2.join()
# print(counter_1.counter)
# print(counter_2.counter)

#РЕЗУЛЬТАТ 1000000

#=========================================================== 2 =========================================================
"""Task 2

Echo server with threading

Create a socket echo server which handles each connection in a separate Thread"""
# import socket, threading
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
# HOST = 'localhost'
# PORT = 8888
#
# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server_address = (HOST, PORT)
# print('starting up --- TCP SERVER --- on {} port {}'.format(*server_address))
# server.bind(server_address)
#
# server.listen(5)
# threadings_list =[]
#
# while True:
#     # Wait for a connection
#     print('waiting for a connection')
#     connection, client_address = server.accept()
#     t = threading.Thread(target=handle_connection, args=(connection, client_address), daemon=True)
#     threadings_list.append(t)
#     t.start()

#=========================================================== 3 =========================================================
"""Task 3

Requests using multithreading"""

import requests
import threading
import json

currencies_list = ['eur', 'usd', 'gbp']

def get_currency_info(start_date, end_date, currency):

    response = requests.get(f'https://bank.gov.ua/NBU_Exchange/exchange_site?start={start_date}&end={end_date}&valcode={currency}&sort=exchangedate&order=asc&json')
    data = response.json()

    with open(f'{currency}.json', 'w', encoding='utf-8') as fo:
        json.dump(response.json(), fo, indent=4, ensure_ascii=False)



threads_list = []
for currency in currencies_list:
    t = threading.Thread(target=get_currency_info, args=('20250101', '20251001',currency))
    threads_list.append(t)
    t.start()


for t in threads_list:
    t.join()

print("------>All files were created")



