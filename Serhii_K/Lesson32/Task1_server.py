# Task 1:
# На уроці ми створили сервер і клієнт, які використовують протокол TCP/IP для зв'язку через сокети.
# У цьому завданні вам потрібно створити сервер і клієнт,
# які будуть використовувати для зв'язку протокол користувацьких дейтаграм (UDP).

import socket

HOST = 'localhost'
PORT = 65432

while True:
    # В циклі while створюємо сокет для постійної готовності сервера до нових підключень:
    # Використовуємо контекстний менеджер with:
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((HOST, PORT))
        print('waiting for a connection')
        # В циклі while отримуємо дані від відправника, декодуємо їх, відправляємо повідомлення назад
        # та перевіряємо чи не надійшла команда на закриття сервера:
        while True:
            try:
                data, addr = s.recvfrom(1024)
            except:
                break
            print('Connected by', addr)
            if not data:
                print('no data from', addr)
                break

            # Декодування та друк отриманих даних (для наглядної перевірки)
            data_string = data.decode('UTF-8')
            print(f"Server received: {data_string}")

            # Повернення даних назад:
            string2 = f"Server send back: {data_string}"
            s.sendto(string2.encode("utf-8"), addr)

            # Якщо отримано команду на закриття сервера
            if data_string == 'close_server':
                print('Server stoped')
                quit()