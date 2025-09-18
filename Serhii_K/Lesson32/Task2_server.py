# Task 2:
# Розширити ехо-сервер, який повертає клієнту дані,
# зашифровані за допомогою алгоритму шифру Цезаря певним ключем, отриманим від клієнта.
import socket
from Task2_Caesar import Caesar_cipher

if __name__ == '__main__':
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

                # Якщо отримано команду на закриття сервера
                if data_string == 'stop_server':
                    print('Server stoped')
                    quit()
                else:
                    # Розділяємо повідомлення на ключ і текст:
                    x = data_string.index(".")  # Індекс крапки в рядку
                    key = int(data_string[:x])
                    text = data_string[(x + 1):]
                    # Використання шифру Цезаря
                    new_string = Caesar_cipher(text, key)
                    # Повернення зашифрованих даних назад:
                    s.sendto(new_string.encode("utf-8"), addr)
                    print(f"Server send back: {new_string}")
