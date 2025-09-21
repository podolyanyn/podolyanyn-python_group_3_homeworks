import socket

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    # Відправка даних до сервера:
    # s.sendto('Привіт'.encode('UTF-8'), (HOST, PORT))        # Просте повідомлення
    s.sendto('close_server'.encode('UTF-8'), (HOST, PORT))  # команда на закриття сервера

    # Отримання повідомлення від сервера:
    data = s.recv(1024).decode('UTF-8')

print('Received', repr(data))