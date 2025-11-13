import json
import os
from typing import List, Dict

PHONEBOOK_FILE = "phonebook.json"

def load_phonebook() -> List[Dict[str, str]]:
    if not os.path.exists(PHONEBOOK_FILE):
        with open(PHONEBOOK_FILE, 'w') as file:
            json.dump([], file)
        return []
    with open(PHONEBOOK_FILE, 'r') as file:
        return json.load(file)

def save_phonebook(contacts: List[Dict[str, str]]) -> None:
    with open(PHONEBOOK_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)

def add_entry(contacts: List[Dict[str, str]], first_name: str, last_name: str, phone: str, city: str, state: str) -> None:
    entry: Dict[str, str] = {
        "phone": phone,
        "first_name": first_name,
        "last_name": last_name,
        "city": city,
        "state": state
    }

    contacts.append(entry)
    print("Entry added successfully!")

def search_by_first_name(contacts: List[Dict[str, str]], first_name: str) -> List[Dict[str, str]]:
    return [contact for contact in contacts if contact["first_name"].lower() == first_name.lower()]

def search_by_last_name(contacts: List[Dict[str, str]], last_name: str) -> List[Dict[str, str]]:
    return [contact for contact in contacts if contact["last_name"].lower() == last_name.lower()]

def search_by_full_name(contacts: List[Dict[str, str]], first_name: str, last_name: str) -> List[Dict[str, str]]:
    return [contact for contact in contacts
            if contact["first_name"].lower() == first_name.lower()
            and contact["last_name"].lower() == last_name.lower()]

def search_by_phone(contacts: List[Dict[str, str]], phone: str) -> List[Dict[str, str]]:
    return [contact for contact in contacts if contact["phone"] == phone]

def search_by_city_or_state(contacts: List[Dict[str, str]], location: str) -> List[Dict[str, str]]:
    return [contact for contact in contacts
            if contact["city"].lower() == location.lower() or contact["state"].lower() == location.lower()]

def delete_by_phone(contacts: List[Dict[str, str]], phone: str) -> bool:
    init_len: int = len(contacts)
    contacts[:] = [contact for contact in contacts if contact["phone"] != phone]
    return len(contacts) < init_len

def update_by_phone(contacts: List[Dict[str, str]], phone: str, first_name: str, last_name: str, city: str, state: str) -> bool:
    for contact in contacts:
        if contact["phone"] == phone:
            contact.update({
                "phone": phone,
                "first_name": first_name,
                "last_name": last_name,
                "city": city,
                "state": state
            })
            return True
    return False

def print_contacts(contacts: List[Dict[str, str]]) -> None:
    if not contacts:
        print("No contacts found.")
        return
    for contact in contacts:
        print(f"Phone: {contact['phone']}, Name: {contact['first_name']} {contact['last_name']}, "
              f"City: {contact['city']}, State: {contact['state']}")

def main() -> None:
    contacts: List[Dict[str, str]] = load_phonebook()

    while True:
        print("\nPhonebook Menu:")
        print("1. Add new entry")
        print("2. Search by first name")
        print("3. Search by last name")
        print("4. Search by full name")
        print("5. Search by phone number")
        print("6. Search by city or state")
        print("7. Delete by phone number")
        print("8. Update by phone number")
        print("9. Exit")

        choice: str = input("Enter choice (1-9): ")

        if choice == "1":
            first_name: str = input("Enter first name: ")
            last_name: str = input("Enter last name: ")
            phone: str = input("Enter phone number: ")
            city: str = input("Enter city: ")
            state: str = input("Enter state: ")
            add_entry(contacts, first_name, last_name, phone, city, state)

        elif choice == "2":
            first_name: str = input("Enter first name to search: ")
            results: List[Dict[str, str]] = search_by_first_name(contacts, first_name)
            print_contacts(results)

        elif choice == "3":
            last_name: str = input("Enter last name to search: ")
            results: List[Dict[str, str]] = search_by_last_name(contacts, last_name)
            print_contacts(results)

        elif choice == "4":
            first_name: str = input("Enter first name: ")
            last_name: str = input("Enter last name: ")
            results: List[Dict[str, str]] = search_by_full_name(contacts, first_name, last_name)
            print_contacts(results)

        elif choice == "5":
            phone: str = input("Enter phone number to search: ")
            results: List[Dict[str, str]] = search_by_phone(contacts, phone)
            print_contacts(results)

        elif choice == "6":
            location: str = input("Enter city or state to search: ")
            results: List[Dict[str, str]] = search_by_city_or_state(contacts, location)
            print_contacts(results)

        elif choice == "7":
            phone: str = input("Enter phone number to delete: ")
            if delete_by_phone(contacts, phone):
                print("Entry deleted successfully!")
            else:
                print("No entry found with that phone number.")

        elif choice == "8":
            phone: str = input("Enter phone number to update: ")
            first_name: str = input("Enter new first name: ")
            last_name: str = input("Enter new last name: ")
            city: str = input("Enter new city: ")
            state: str = input("Enter new state: ")
            if update_by_phone(contacts, phone, first_name, last_name, city, state):
                print("Entry updated successfully!")
            else:
                print("No entry found with that phone number.")

        elif choice == "9":
            save_phonebook(contacts)
            print("Phonebook saved. Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()