# Task 3:
# Ехо-сервер з asyncio
# Створіть ехо-сервер сокетів, який обробляє кожне з'єднання за допомогою асинхронних завдань.

import asyncio

# Подія для зупинки сервера після надходження команди на зупинку сервера
stop_event = asyncio.Event()

async def my_func(reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
    # reader: asyncio.StreamReader - об’єкт, з якого можна асинхронно читати дані, що надійшли від клієнта
    # writer: asyncio.StreamWriter - об’єкт, у який можна записати дані й відправити їх клієнту
    try:
        data = await reader.read(1024)
        if not data:
            return

        # Отримання повідомлення від клієнта
        message = data.decode("UTF-8")
        print(f"Received data: {message}")

        if message == "stop_server":
            # Встановлюємо подію зупинки
            stop_event.set()
            response = "Stopping server..."
        else:
            # Відповідь у верхньому регістрі
            response = message.upper()
            print(f"Send data: {response}")

        # Відправлення відповіді клієнту:
        writer.write(response.encode("UTF-8"))

        # Очікування поки всі дані, що передані в writer.write,
        # не будуть реально записані в мережевий буфер і відправлені клієнту
        # (завжди після writer.write(...) треба робити await writer.drain()) - ChatGPT
        await writer.drain()

    finally:
        writer.close()              # Команда на закриття TCP-з’єднання
        await writer.wait_closed()  # Очікування, поки сокет дійсно закриється


async def main():
    HOST = '127.0.0.1'
    PORT = 65432

    # Створення сервера
    server = await asyncio.start_server(my_func, HOST, PORT)

    async with server:              # Запуск сервера
        print('Waiting for connection...')
        await stop_event.wait()     # Це головна подія очікування події stop_event (замість циклу while)
        print("Stopping server...")
        server.close()              # Зупинка прийняття нових підключень
        await server.wait_closed()  # Очікування поки всі відкриті сокети сервера закриються


if __name__ == "__main__":
    asyncio.run(main())
