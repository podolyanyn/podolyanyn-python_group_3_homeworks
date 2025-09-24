# Task 2:
# Ехо-сервер з threading
# Створіть ехо-сервер сокетів, який обробляє кожне з'єднання в окремому потоці

import socket
import threading

Server_work = True # Глобальна змінна - флаг зупинки сервера

def conn_proc(conn, addr):
    """Функція, що отримує підключення з клієнтом,
    отримує від клієнта повідомлення,
    обробляє його і надсилає назад відповідь.
    Для використання в окремих потоках"""

    global Server_work  # Використання глобальної змінної Server_work

    text = ''
    with conn:
        print('Connected by', addr)

        # Отримання повідомлення
        data = conn.recv(1024).decode('UTF-8')
        print('received data:', data)

        # Якщо отримана команда на зупинку сервера, то змінюємо флаг Stop_server на True,
        # створюємо та відправляємо зворотне повідомлення про зупинку сервера:
        if data == 'stop_server':
            Server_work = False
            data = 'Stopping server...'
            conn.sendall(data.encode('UTF-8'))

        # Або створюємо та відправляємо зворотне повідомлення в верхньому регістрі:
        else:
            # Переводимо рядок в верхній регістр
            text = data.upper()

            # Повертаємо назад повідомлення
            conn.sendall(text.encode('UTF-8'))
            print(f'Send data: {text}')



if __name__ == '__main__':
    HOST = '127.0.0.1'
    PORT = 65432

    # З використанням контекстного менеджера with створюємо сокет:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind((HOST, PORT))
        sock.listen()

        # Коли отримано повідомлення про зупинку сервера, то один з потоків,
        # що обробляє це повідомлення, змінить флаг Server_work на False.
        # Але цього буде замало для зупинки сервера, бо sock.accept() чекає нового підключення (на цей час блокує програму).
        # Тому додаємо до сокета таймаут 1 секунду - тепер, якщо ніхто не підключився за 1 секунду,
        # sock.accept() викине socket.timeout, і цикл піде далі і зможе перевірити Server_work і завершитись (ChatGPT)
        sock.settimeout(1)

        print('Waiting for connection...')

        # Цикл працює поки Server_work не дорівнює False
        while Server_work:
            # Спроба підключення, але з таймаутом 1 секунду:
            try:
                # Отримуємо підключення:
                conn, addr = sock.accept()  #<<-- Саме тут очікується нове підключення поки діє таймаут,
                                            # або спрацьовує таймаут і sock.accept() ініціює виключення

                # Створюємо потік виконання і запускаємо його:
                t = threading.Thread(target=conn_proc, args=(conn, addr))
                # print('Thread name = ', t.name)
                t.start()

            except socket.timeout:
                continue

        # t.join() для очікування завершення роботи всіх потоків не використовуємо, бо для сервера це не потрібно

        # Якщо виконання програми дійшло до цього рядка -
        # це означає, що Server_work змінився на False,
        # цикл while завершився і сервер більше не працює.
        # Друкуємо повідомлення про зупинку сервера:
        print('Server stopped.')