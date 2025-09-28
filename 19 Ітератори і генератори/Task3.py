import unittest
import json
import os
import tempfile

def add_contact(pb, phone, first_name, last_name, city, state):
    """Додає новий контакт у телефонну книгу."""
    if not phone:
        print("Номер телефону не може бути порожнім.")
        return
    if phone in pb:
        print("Такий номер вже існує.")
        return
    pb[phone] = {
        "first_name": first_name,
        "last_name": last_name,
        "city": city,
        "state": state
    }
    print("Контакт додано.")

def search(pb, phone):
    """Шукає контакт за номером телефону."""
    return pb.get(phone, None)

def search_full_name(pb, first_name, last_name):
    """Шукає контакт за повним ім'ям."""
    results = []
    for phone, info in pb.items():
        if info["first_name"] == first_name and info["last_name"] == last_name:
            results.append((phone, info))
    return results

def delete_contact(pb, phone):
    """Видаляє контакт з телефонної книги."""
    if phone in pb:
        del pb[phone]
        print("Контакт видалено.")
        return True
    print("Контакт не знайдено.")
    return False

def update_contact(pb, phone, first_name=None, last_name=None, city=None, state=None):
    """Оновлює дані контакту."""
    if phone in pb:
        if first_name:
            pb[phone]["first_name"] = first_name
        if last_name:
            pb[phone]["last_name"] = last_name
        if city:
            pb[phone]["city"] = city
        if state:
            pb[phone]["state"] = state
        print("Контакт оновлено.")
        return True
    print("Контакт не знайдено.")
    return False

def save_data(pb, filename):
    """Зберігає телефонну книгу у файл."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(pb, f, ensure_ascii=False, indent=4)
    print("Дані збережено.")

def load_data(filename):
    """Завантажує телефонну книгу з файлу."""
    if os.path.exists(filename):
        try:
            with open(filename, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            print(f"Файл '{filename}' пошкоджений або не є валідним JSON.")
            return {}
    return {}



class TestPhonebook(unittest.TestCase):
    def setUp(self):
        self.pb = {
            "123": {
                "first_name": "Микола",
                "last_name": "Максименко",
                "city": "Київ",
                "state": "Київська"
            }
        }

    def test_add_contact(self):
        add_contact(self.pb, "456", "Іван", "Іваненко", "Львів", "Львівська")
        self.assertIn("456", self.pb)
        self.assertEqual(self.pb["456"]["city"], "Львів")

    def test_search(self):
        result = search(self.pb, "123")
        self.assertIsNotNone(result)
        self.assertEqual(result["first_name"], "Микола")

    def test_search_full_name(self):
        results = search_full_name(self.pb, "Микола", "Максименко")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0][0], "123")

    def test_delete_contact(self):
        delete_contact(self.pb, "123")
        self.assertNotIn("123", self.pb)

    def test_update_contact(self):
        update_contact(self.pb, "123", first_name="Олег")
        self.assertEqual(self.pb["123"]["first_name"], "Олег")

    def test_save_and_load_data(self):
        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            filename = tmp.name
        try:
            save_data(self.pb, filename)
            loaded_pb = load_data(filename)
            self.assertEqual(self.pb, loaded_pb)
        finally:
            os.remove(filename)

# ---------------- Запуск тестів ----------------
if __name__ == "__main__":
    unittest.main()