import sys
import json
import os

def load_data(filename):
    if not os.path.exists(filename):
        print(f"❌ Помилка: файл '{filename}' не знайдено.")
        sys.exit(1)
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_data(data, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def show_menu():
    print("\n📖 Меню телефонної книги:")
    print("1. Додати новий контакт")
    print("2. Пошук за ім'ям")
    print("3. Пошук за прізвищем")
    print("4. Пошук за повним ім'ям")
    print("5. Пошук за номером")
    print("6. Пошук за містом або областю")
    print("7. Видалити контакт")
    print("8. Оновити контакт")
    print("9. Вихід")

def print_contact(phone, data):
    print(f"📞 {phone} — {data['first_name']} {data['last_name']} ({data['city']}, {data['state']})")

def add_contact(phonebook):
    phone = input("Введи номер телефону: ")
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

def run_phonebook(filename):
    phonebook = load_data(filename)

    while True:
        show_menu()
        choice = input("Вибір: ")
        if choice == "1":
            add_contact(phonebook)
        elif choice == "2":
            name = input("Ім'я: ")
            results = search(phonebook, "first_name", name)
            for phone, data in results:
                print_contact(phone, data)
        elif choice == "3":
            surname = input("Прізвище: ")
            results = search(phonebook, "last_name", surname)
            for phone, data in results:
                print_contact(phone, data)
        elif choice == "4":
            full = input("Повне ім’я (Ім’я Прізвище): ")
            results = search_full_name(phonebook, full)
            for phone, data in results:
                print_contact(phone, data)
        elif choice == "5":
            phone = input("Номер: ")
            if phone in phonebook:
                print_contact(phone, phonebook[phone])
            else:
                print("❌ Не знайдено.")
        elif choice == "6":
            region = input("Місто або область: ")
            results = search(phonebook, "city", region) + search(phonebook, "state", region)
            for phone, data in results:
                print_contact(phone, data)
        elif choice == "7":
            delete_contact(phonebook)
        elif choice == "8":
            update_contact(phonebook)
        elif choice == "9":
            save_data(phonebook, filename)
            print("💾 Дані збережено. До зустрічі!")
            break
        else:
            print("❗ Невірна команда")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("❗ Укажіть назву JSON-файлу: python phonebook.py book.json")
        sys.exit(1)

    file = sys.argv[1]
    run_phonebook(file)