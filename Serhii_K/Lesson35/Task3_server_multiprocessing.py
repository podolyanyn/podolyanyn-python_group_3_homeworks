# Task 3:
# Ехо-сервер з multiprocessing
# Створіть ехо-сервер сокетів, який обробляє кожне з'єднання за допомогою бібліотеки multiprocessing.

import socket
import multiprocessing

def conn_proc(conn, addr, stop_event):
    """Функція отримує підключення з клієнтом, його адресу, а також подію stop_event (multiprocessing.Event() для її використання у випадку зупинки сервера).
    Під час роботи функція отримує від клієнта текстове повідомлення, обробляє його і надсилає назад відповідь у верхньому регістрі.
    У випадку отримання текстового повідомлення на зупинку сервера - активується подія stop_event (multiprocessing.Event())
    Для використання в окремих процесах"""

    text = ''
    with conn:
        print('Connected by', addr)

        # Отримання повідомлення:
        data = conn.recv(1024).decode('UTF-8')
        print('received data:', data)

        # Перевіряємо зміст отриманого повідомлення:
        if data == 'stop_server':
            # Якщо отримана команда на зупинку сервера, то активуємо подію stop_event:
            stop_event.set()
            # а також відправляємо зворотне повідомлення про зупинку сервера:
            conn.sendall('Stopping server...'.encode('UTF-8'))

        # Або створюємо та відправляємо зворотне повідомлення в верхньому регістрі:
        else:
            # Переводимо рядок в верхній регістр:
            text = data.upper()

            # Повертаємо повідомлення назад клієнту:
            conn.sendall(text.encode('UTF-8'))
            print(f'Send data: {text}')



if __name__ == '__main__':
    HOST = '127.0.0.1'
    PORT = 65432

    # Створюємо подію для використання у випадку отримання команди на зупинку сервера:
    stop_event = multiprocessing.Event()

    # З використанням контекстного менеджера with створюємо сокет:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind((HOST, PORT))
        sock.listen()

        # Коли отримано повідомлення про зупинку сервера, то одним з процессів буде викликана подія stop_event.
        # Але цього буде замало для зупинки сервера, бо sock.accept() чекає нового підключення (на цей час блокує програму).
        # Тому додаємо до сокета таймаут 1 секунду - тепер, якщо ніхто не підключився за 1 секунду,
        # sock.accept() викине socket.timeout, і цикл піде далі і зможе перевірити чи активована подія stop_event:
        sock.settimeout(1)

        print('Waiting for connection...')

        # Цикл працює поки не викликана подія зупинки сервера:
        while stop_event.is_set() == False:
            # Спроба підключення, але з таймаутом 1 секунду:
            try:
                # Отримуємо підключення:
                conn, addr = sock.accept()  #<<-- Саме тут очікується нове підключення поки діє таймаут,
                                            # або спрацьовує таймаут і sock.accept() ініціює виключення

                # Створюємо процес виконання і запускаємо його:
                p = multiprocessing.Process(target=conn_proc, args=(conn, addr, stop_event))
                p.start()

            # Якщо спрацював таймаут - повертаємось на початок циклу:
            except socket.timeout:
                continue

        # Якщо виконання програми дійшло до цього рядка -
        # це означає, що stop_event.is_set() == True,
        # цикл while завершився і сервер більше не працює.
        # Друкуємо повідомлення про зупинку сервера:
        print('Server stopped.')