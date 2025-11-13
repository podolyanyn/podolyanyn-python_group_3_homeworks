import httpx
import time
from parsel import Selector
import asyncio  # Потрібен для запуску async-функцій

# ==================== КОНФІГУРАЦІЯ ====================
BASE_URL = "http://127.0.0.1:8000"
LOGIN_URL = "/accounts/login/"
NOTE_ID = 23  # ID нотатки для тестування

LOGIN_CREDENTIALS = {
    "username": "user_2",
    "password": "superuser1234",
}

# Дані для POST-запитів
NEW_NOTE_DATA = {
    "note_category": "Тест швидкості Async",
    "note_title": "Нова нотатка для тесту Async",
    "note_text": "Текст нової нотатки для вимірювання часу Async.",
    "note_reminder": "2026-11-30 10:00",
}

EDIT_NOTE_DATA = {
    "note_category": "Тест швидкості Async",
    "note_title": "ОНОВЛЕНО: Тестова нотатка Async",
    "note_text": "Текст змінено для вимірювання часу Async.",
    "note_reminder": "2026-11-30 11:00",
}


# ==================== УТИЛІТИ ========================

async def get_csrf_token(client, url_path):
    """Асинхронно отримує CSRF-токен зі сторінки форми."""
    try:
        # Використовуємо await для асинхронного запиту
        response = await client.get(url_path)
        selector = Selector(text=response.text)
        token = selector.css('input[name="csrfmiddlewaretoken"]::attr(value)').get()
        return token
    except httpx.RequestError as e:
        print(f"❌ Помилка при отриманні CSRF-токену з {url_path}: {e}")
        return None


async def execute_request_async(client, name, method, url_path, data=None):
    """Виконує асинхронний запит, вимірює час і друкує результат."""
    try:
        start_time = time.time()

        if method == "GET":
            # Асинхронний GET
            response = await client.get(url_path)
        elif method == "POST":
            # Асинхронний POST
            response = await client.post(url_path, data=data)
        else:
            raise ValueError(f"Непідтримуваний метод: {method}")

        response.raise_for_status()
        elapsed_time = time.time() - start_time

        # Перевірка статусу відповіді
        status = "✅ OK" if response.status_code in [200, 302] else f"❌ Status {response.status_code}"

        print(f"| {name.ljust(35)} | {method.ljust(6)} | {elapsed_time:.6f} | {status}")
        return response

    except httpx.HTTPStatusError as e:
        print(f"| {name.ljust(35)} | {method.ljust(6)} | {'N/A':<8} | ❌ Error {e.response.status_code}")
    except httpx.RequestError:
        print(f"| {name.ljust(35)} | {method.ljust(6)} | {'N/A':<8} | ❌ Request Error")
    except Exception as e:
        print(f"| {name.ljust(35)} | {method.ljust(6)} | {'N/A':<8} | ❌ Exception ({type(e).__name__})")

    return None


async def measure_async_once():
    print("Початок АСИНХРОННОГО тестування...")

    async with httpx.AsyncClient(base_url=BASE_URL, follow_redirects=True, timeout=30.0) as client:

        # 1. АВТЕНТИФІКАЦІЯ
        print("1. Авторизація користувача...")

        # Отримання токена асинхронно
        login_token = await get_csrf_token(client, LOGIN_URL)
        if not login_token: return

        login_data = {**LOGIN_CREDENTIALS, "csrfmiddlewaretoken": login_token}
        response = await client.post(LOGIN_URL, data=login_data)

        if LOGIN_URL in str(response.url) or response.status_code != 200:
            print("   ❌ Логін не вдалося. Перевірте облікові дані або URL.")
            return

        print("   ✅ Логін успішний.\n")



        # 2. ПОСЛІДОВНЕ ВИКОНАННЯ ЗАПИТІВ (згруповано)
        print("-" * 75)
        print(f"| {'Endpoint':<35} | {'Метод':<6} | {'Час (с)':<8} | {'Статус':<15}")
        print("-" * 75)

        temp_note_id = NOTE_ID

        # 1. index (Список нотаток)
        await execute_request_async(client, "index (Список нотаток)", "GET", f"/notes/")

        # 2. detail_note (Деталі нотатки)
        await execute_request_async(client, "detail_note (Деталі нотатки)", "GET", f"/notes/{temp_note_id}/")

        # 3. add_note (Форма додавання) - GET
        await execute_request_async(client, "add_note (Форма додавання)", "GET", f"/notes/add_note/")

        # 4. POST: add_note - POST
        add_token = await get_csrf_token(client, "/notes/add_note/")
        if add_token:
            add_data = {**NEW_NOTE_DATA, "csrfmiddlewaretoken": add_token}
            await execute_request_async(client, "add_note (POST: Створення)", "POST", "/notes/add_note/", data=add_data)

        # 5. edit_note (Форма редагування) - GET
        await execute_request_async(client, "edit_note (Форма редагування)", "GET", f"/notes/{temp_note_id}/edit/")

        # 6. POST: edit_note - POST
        edit_token = await get_csrf_token(client, f"/notes/{temp_note_id}/edit/")
        if edit_token:
            edit_data = {**EDIT_NOTE_DATA, "csrfmiddlewaretoken": edit_token}
            await execute_request_async(client, "edit_note (POST: Зміна)", "POST", f"/notes/{temp_note_id}/edit/",
                                        data=edit_data)

        print("-" * 75)


if __name__ == "__main__":
    # Запускаємо асинхронну головну функцію
    asyncio.run(measure_async_once())