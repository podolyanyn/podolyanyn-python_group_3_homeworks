# Завдання 1
# Під час уроку ми створили сервер і клієнт, які використовують протокол TCP/IP для зв'язку через сокети.'
# (' У цьому завданні вам потрібно створити сервер і клієнт, які використовуватимуть протокол користувацьких дейтаграм (UDP) '
 # 'для зв'язку.)
# import socket
#
# HOST = 'localhost'
# PORT = 8080
#
# with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
#
#     s.sendto(b'Putin h***lo', (HOST, PORT))
#
#
#
#     data, server = s.recvfrom(1024)
#
# print('Received', repr(data))

# Завдання 2
#
# Розширити echo-сервер, який повертає клієнту дані, зашифровані за допомогою алгоритму шифрування
# Цезаря за допомогою певного ключа, отриманого від клієнта.

import pickle
import socket
text = ('20240123','20250924','eur')
HOST ='localhost'
PORT = 8082

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    tuple_for_send = pickle.dumps(text)

    s.sendall(tuple_for_send)
    data: bytes = s.recv(100000)
    received_data = pickle.loads(data)
print('Received', repr(received_data))

# import pickle
# import socket
# text = ('20250923','20250924','usd')
# HOST ='localhost'
# PORT = 8080
#
# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.connect((HOST, PORT))
#     tuple_for_send = pickle.dumps(text)
#
#     s.sendall(tuple_for_send)
#     data: bytes = s.recv(1024)
#     received_data = pickle.loads(data)
# print('Received', repr(received_data))

