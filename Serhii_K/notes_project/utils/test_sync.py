import httpx
import time
from parsel import Selector


BASE_URL = "http://127.0.0.1:8000"
LOGIN_URL = "/accounts/login/"
NOTE_ID = 23  # ID нотатки для тестування

# Дані реального зареєстрованого користувача;
LOGIN_CREDENTIALS = {
    "username": "user_2",
    "password": "superuser1234",
}

# Дані для POST-запитів
NEW_NOTE_DATA = {
    "note_category": "Тест швидкості",
    "note_title": "Нова нотатка для тесту",
    "note_text": "Текст нової нотатки для вимірювання часу.",
    "note_reminder": "2026-11-30 10:00",
}

EDIT_NOTE_DATA = {
    "note_category": "Тест швидкості",
    "note_title": "ОНОВЛЕНО: Тестова нотатка",
    "note_text": "Текст змінено для вимірювання часу.",
    "note_reminder": "2026-11-30 11:00",
}



def get_csrf_token(client, url_path):
    """Отримує CSRF-токен зі сторінки форми за допомогою GET-запиту (підказка Gemini)"""
    try:
        response = client.get(url_path)
        selector = Selector(text=response.text)
        token = selector.css('input[name="csrfmiddlewaretoken"]::attr(value)').get()
        return token
    except httpx.RequestError as e:
        print(f"❌ Помилка при отриманні CSRF-токену з {url_path}: {e}")
        return None


def execute_request(client, name, method, url_path, data=None):
    try:
        start_time = time.time()

        if method == "GET":
            response = client.get(url_path)
        elif method == "POST":
            response = client.post(url_path, data=data)
        else:
            raise ValueError(f"Непідтримуваний метод: {method}")

        response.raise_for_status()
        elapsed_time = time.time() - start_time

        # Перевірка статусу відповіді (підказка Gemini):
        status = "✅ OK" if response.status_code in [200, 302] else f"❌ Status {response.status_code}"

        print(f"| {name.ljust(35)} | {method.ljust(6)} | {elapsed_time:.6f} | {status}")
        return response

    except httpx.HTTPStatusError as e:
        # Обробка помилок HTTP
        print(f"| {name.ljust(35)} | {method.ljust(6)} | {'N/A':<8} | ❌ Error {e.response.status_code}")
    except httpx.RequestError:
        # Обробка помилок мережі або інших проблем із запитом
        print(f"| {name.ljust(35)} | {method.ljust(6)} | {'N/A':<8} | ❌ Request Error")
    except Exception as e:
        # Загальна обробка помилок
        print(f"| {name.ljust(35)} | {method.ljust(6)} | {'N/A':<8} | ❌ Exception ({type(e).__name__})")

    return None


def measure_sync():
    print("Початок тестування...")

    with httpx.Client(base_url=BASE_URL, follow_redirects=True, timeout=30.0) as client:

        # АВТЕНТИФІКАЦІЯ
        print("1. Авторизація користувача...")
        login_token = get_csrf_token(client, LOGIN_URL)
        if not login_token: return

        login_data = {**LOGIN_CREDENTIALS, "csrfmiddlewaretoken": login_token}
        response = client.post(LOGIN_URL, data=login_data)

        if LOGIN_URL in str(response.url) or response.status_code != 200:
            print("Логін не вдалося. Перевірте облікові дані або URL.")
            return

        print("Логін успішний.\n")



        # ПОСЛІДОВНЕ ВИКОНАННЯ ЗАПИТІВ
        print("-" * 75)
        print(f"| {'Endpoint':<35} | {'Метод':<6} | {'Час (с)':<8} | {'Статус':<15}")
        print("-" * 75)

        # 1. index (Список нотаток)
        execute_request(client, "index (Список нотаток)", "GET", f"/notes/")

        # 2. detail_note (Деталі нотатки)
        execute_request(client, "detail_note (Деталі нотатки)", "GET", f"/notes/{NOTE_ID}/")

        # 3. add_note (Форма додавання) - GET
        execute_request(client, "add_note (Відкриття форми)", "GET", f"/notes/add_note/")

        # 4. POST: add_note - POST
        add_token = get_csrf_token(client, "/notes/add_note/")
        if add_token:
            add_data = {**NEW_NOTE_DATA, "csrfmiddlewaretoken": add_token}
            execute_request(client, "add_note (POST: Створення)", "POST", "/notes/add_note/", data=add_data)

        # 5. edit_note (Форма редагування) - GET
        execute_request(client, "edit_note (Відкриття форми)", "GET", f"/notes/{NOTE_ID}/edit/")

        # 6. POST: edit_note - POST
        edit_token = get_csrf_token(client, f"/notes/{NOTE_ID}/edit/")
        if edit_token:
            edit_data = {**EDIT_NOTE_DATA, "csrfmiddlewaretoken": edit_token}
            execute_request(client, "edit_note (POST: Зміна)", "POST", f"/notes/{NOTE_ID}/edit/", data=edit_data)

        print("-" * 75)


if __name__ == "__main__":
    measure_sync()



# Результати тестування синхронних views:
    # Час виконання index (Список нотаток)              = 0.05  - 0.11 сек.
    # Час виконання detail_note (Деталі нотатки)        = 0.009 - 0.01 сек.
    # Час виконання add_note (Відкриття форми)          = 0.011 - 0.021 сек.
    # Час виконання add_note (POST: Збереження)         = 0.16  - 0.22 сек.
    # Час виконання edit_note (Відкриття форми)         = 0.011 - 0.015 сек.
    # Час виконання edit_note (POST: Зміна)             = 0.10  - 0.15 сек.

# Результати тестування асинхронних views:
    # Час виконання index (Список нотаток)              = 0.06  - 0.10 сек.
    # Час виконання detail_note (Деталі нотатки)        = 0.012 - 0.016 сек.
    # Час виконання add_note (Відкриття форми)          = 0.011 - 0.015 сек.
    # Час виконання add_note (POST: Збереження)         = 0.20  - 0.25 сек.
    # Час виконання edit_note (Відкриття форми)         = 0.014 - 0.020 сек.
    # Час виконання edit_note (POST: Зміна)             = 0.10  - 0.18 сек.


# Висновок: Використання асинхронного підходу практично не прискорює виконання функцій views,
# а в деяких випадках навіть сповільнює виконання (під час звернення до бази даних - POST-запити).
# Але при великій кількості параллельних користувачів асинхронний підхід може збільшити пропускну здатність сайту.
