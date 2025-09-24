# Клієнт для перевірки роботи сервера, що обробляє кожне з'єднання в окремому потоці
# (Це не входить в умови завдання Task 2 !!!)

import socket
import threading

HOST = '127.0.0.1'
PORT = 65432

def conn_proc(message):
    """Функція, що отримує повідомлення і надсилає його до сервера.
        Для використання в окремих потоках"""
    try:
        # Створюємо підключення до серверу, передаємо повідомлення і отримуємо відповідь:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((HOST, PORT))
            sock.sendall(message.encode('UTF-8'))
            print("Надіслано:", message)
            data = sock.recv(1024).decode('UTF-8')
            print('Отримано:', data)
    except:
        pass    # Тут нічого не робимо, потрібно лише щоб помилки не зупиняли програму..

if __name__ == '__main__':
    # Список повідомлень до сервера:
    list1 = ['Кропива',  'Тополя', 'Білочка', 'Зайчик', 'Котик']

    list_threads = []   # Список потоків
    for message in list1:
        # Створюємо потік виконання, додаємо його до списку і запускаємо:
        t = threading.Thread(target=conn_proc, args=(message,))
        list_threads.append(t)
        t.start()

    # Чекаємо поки кожний потік завершить роботу:
    for t in list_threads:
        t.join()

    # В кінці передаємо на сервер команду на його зупинку:
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            s.sendall('stop_server'.encode('UTF-8'))
            print('Надіслана команда на зупинку сервера...')
            data = s.recv(1024).decode('UTF-8')
            print('Отримано:', data)
    except:
        pass

