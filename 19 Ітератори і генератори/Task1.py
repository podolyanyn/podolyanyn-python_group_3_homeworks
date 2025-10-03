import unittest
from unittest.mock import patch
from io import StringIO
import os
import json
import tempfile

# Функції з програми «Телефонна книга»
def load_data(filename):
    if not os.path.exists(filename):
        print(f"❌ Помилка: файл '{filename}' не знайдено.")
        return {}
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError:
        print(f"❌ Помилка: файл '{filename}' пошкоджений або не є валідним JSON.")
        return {}

def save_data(data, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print("💾 Дані збережено.")

def show_menu():
    print("\n📖 Меню телефонної книги:")
    print("1. Додати новий контакт")
    print("2. Пошук за ім'ям")
    print("3. Пошук за прізвищем")
    print("4. Пошук за повним ім'ям")
    print("5. Пошук за номером телефону")
    print("6. Пошук за містом або штатом")
    print("7. Видалити контакт")
    print("8. Оновити контакт")
    print("9. Вихід")

def print_contact(phone, data):
    print(f"📞 {phone} — {data['first_name']} {data['last_name']} ({data['city']}, {data['state']})")

def add_contact(phonebook):
    phone = input("Введи номер телефону: ")
    if not phone:
        print("⛔ Номер телефону не може бути порожнім.")
        return
    if phone in phonebook:
        print("⛔ Такий номер вже існує.")
        return
    contact = {
        "first_name": input("Ім'я: "),
        "last_name": input("Прізвище: "),
        "city": input("Місто: "),
        "state": input("Область/Штат: ")
    }
    phonebook[phone] = contact
    print("✅ Контакт додано.")

def search(phonebook, key, value):
    results = []
    for phone, info in phonebook.items():
        if info.get(key, '').lower() == value.lower():
            results.append((phone, info))
    return results

def search_full_name(phonebook, full_name):
    results = []
    for phone, info in phonebook.items():
        if f"{info['first_name']} {info['last_name']}".lower() == full_name.lower():
            results.append((phone, info))
    return results

def delete_contact(phonebook):
    phone = input("Введи номер для видалення: ")
    if phone in phonebook:
        del phonebook[phone]
        print("🗑️ Контакт видалено.")
    else:
        print("🚫 Контакт не знайдено.")

def update_contact(phonebook):
    phone = input("Введи номер для оновлення: ")
    if phone not in phonebook:
        print("🚫 Контакт не знайдено.")
        return
    info = phonebook[phone]
    info['first_name'] = input(f"Ім'я [{info['first_name']}]: ") or info['first_name']
    info['last_name'] = input(f"Прізвище [{info['last_name']}]: ") or info['last_name']
    info['city'] = input(f"Місто [{info['city']}]: ") or info['city']
    info['state'] = input(f"Область/Штат [{info['state']}]: ") or info['state']
    print("🔄 Контакт оновлено.")

# Клас тестів
class TestPhonebook(unittest.TestCase):
    def setUp(self):
        self.temp_file = tempfile.NamedTemporaryFile(mode='w+', delete=False, encoding='utf-8')
        self.temp_file.close()
        self.pb = {}

    def tearDown(self):
        os.unlink(self.temp_file.name)

    @patch('builtins.input', side_effect=['123456', 'Микола', 'Максименко', 'Київ', 'Київська', '123456', 'Іван', 'Іванов', 'Львів', 'Львівська'])
    def test_add_contact_success(self, mock_input):
        add_contact(self.pb)
        self.assertIn('123456', self.pb)
        self.assertEqual(self.pb['123456']['city'], 'Київ')
        with patch('sys.stdout', new=StringIO()) as fake_out:
            add_contact(self.pb)
            self.assertEqual(fake_out.getvalue().strip(), '⛔ Такий номер вже існує.')

    @patch('builtins.input', side_effect=[''])
    def test_add_contact_empty_phone(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            add_contact(self.pb)
            self.assertNotIn('', self.pb)
            self.assertEqual(fake_out.getvalue().strip(), '⛔ Номер телефону не може бути порожнім.')

    @patch('builtins.input', side_effect=['123456'])
    def test_delete_contact_success(self, mock_input):
        self.pb['123456'] = {'first_name': 'Микола', 'last_name': 'Максименко', 'city': 'Київ', 'state': 'Київська'}
        with patch('sys.stdout', new=StringIO()) as fake_out:
            delete_contact(self.pb)
            self.assertNotIn('123456', self.pb)
            self.assertEqual(fake_out.getvalue().strip(), '🗑️ Контакт видалено.')

    @patch('builtins.input', side_effect=['999999'])
    def test_delete_contact_not_found(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            delete_contact(self.pb)
            self.assertEqual(fake_out.getvalue().strip(), '🚫 Контакт не знайдено.')

    @patch('builtins.input', side_effect=['123456', 'Іван', 'Іванов', 'Львів', 'Львівська'])
    def test_update_contact_success(self, mock_input):
        self.pb['123456'] = {'first_name': 'Микола', 'last_name': 'Максименко', 'city': 'Київ', 'state': 'Київська'}
        with patch('sys.stdout', new=StringIO()) as fake_out:
            update_contact(self.pb)
            self.assertEqual(self.pb['123456']['first_name'], 'Іван')
            self.assertEqual(fake_out.getvalue().strip(), '🔄 Контакт оновлено.')

    @patch('builtins.input', side_effect=['999999'])
    def test_update_contact_not_found(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            update_contact(self.pb)
            self.assertEqual(fake_out.getvalue().strip(), '🚫 Контакт не знайдено.')

    def test_search_success(self):
        self.pb['123456'] = {'first_name': 'Микола', 'last_name': 'Максименко', 'city': 'Київ', 'state': 'Київська'}
        results = search(self.pb, 'city', 'Київ')
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0][1]['city'], 'Київ')

    def test_search_full_name_success(self):
        self.pb['123456'] = {'first_name': 'Микола', 'last_name': 'Максименко', 'city': 'Київ', 'state': 'Київська'}
        results = search_full_name(self.pb, 'Микола Максименко')
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0][1]['first_name'], 'Микола')

    def test_load_data_file_not_found(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            result = load_data('nonexistent.json')
            self.assertEqual(result, {})
            self.assertIn("❌ Помилка: файл 'nonexistent.json' не знайдено.", fake_out.getvalue())

    def test_load_data_invalid_json(self):
        with open(self.temp_file.name, 'w', encoding='utf-8') as f:
            f.write('invalid json')
        with patch('sys.stdout', new=StringIO()) as fake_out:
            result = load_data(self.temp_file.name)
            self.assertEqual(result, {})
            self.assertIn(f"❌ Помилка: файл '{self.temp_file.name}' пошкоджений або не є валідним JSON.", fake_out.getvalue())

    def test_save_data(self):
        self.pb['123456'] = {'first_name': 'Микола', 'last_name': 'Максименко', 'city': 'Київ', 'state': 'Київська'}
        with patch('sys.stdout', new=StringIO()) as fake_out:
            save_data(self.pb, self.temp_file.name)
            self.assertIn("💾 Дані збережено.", fake_out.getvalue())
        with open(self.temp_file.name, 'r', encoding='utf-8') as f:
            saved_data = json.load(f)
            self.assertEqual(saved_data, self.pb)

if __name__ == '__main__':
    unittest.main()