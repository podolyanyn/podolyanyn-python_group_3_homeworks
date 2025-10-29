import json
import os
import unittest

PHONEBOOK_FILE = "phonebook.json"

def load_phonebook():
    if not os.path.exists(PHONEBOOK_FILE):
        with open(PHONEBOOK_FILE, 'w') as file:
            json.dump([], file)
        return []
    with open(PHONEBOOK_FILE, 'r') as file:
        return json.load(file)

def save_phonebook(contacts):
    with open(PHONEBOOK_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)

def add_entry(contacts, first_name, last_name, phone, city, state):
    entry = {
        "phone": phone,
        "first_name": first_name,
        "last_name": last_name,
        "city": city,
        "state": state
    }

    contacts.append(entry)
    print("Entry added successfully!")

def search_by_first_name(contacts, first_name):
    return [contact for contact in contacts if contact["first_name"].lower() == first_name.lower()]

def search_by_last_name(contacts, last_name):
    return [contact for contact in contacts if contact["last_name"].lower() == last_name.lower()]

def search_by_full_name(contacts, first_name, last_name):
    return [contact for contact in contacts
            if contact["first_name"].lower() == first_name.lower()
            and contact["last_name"].lower() == last_name.lower()]

def search_by_phone(contacts, phone):
    return [contact for contact in contacts if contact["phone"] == phone]

def search_by_city_or_state(contacts, location):
    return [contact for contact in contacts
            if contact["city"].lower() == location.lower() or contact["state"].lower() == location.lower()]

def delete_by_phone(contacts, phone):
    init_len = len(contacts)
    contacts[:] = [contact for contact in contacts if contact["phone"] != phone]
    return len(contacts) < init_len

def update_by_phone(contacts, phone, first_name, last_name, city, state):
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

def print_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return
    for contact in contacts:
        print(f"Phone: {contact['phone']}, Name: {contact['first_name']} {contact['last_name']}, "
              f"City: {contact['city']}, State: {contact['state']}")

def main():
    contacts = load_phonebook()

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

        choice = input("Enter choice (1-9): ")

        if choice == "1":
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            phone = input("Enter phone number: ")
            city = input("Enter city: ")
            state = input("Enter state: ")
            add_entry(contacts, first_name, last_name, phone, city, state)

        elif choice == "2":
            first_name = input("Enter first name to search: ")
            results = search_by_first_name(contacts, first_name)
            print_contacts(results)

        elif choice == "3":
            last_name = input("Enter last name to search: ")
            results = search_by_last_name(contacts, last_name)
            print_contacts(results)

        elif choice == "4":
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            results = search_by_full_name(contacts, first_name, last_name)
            print_contacts(results)

        elif choice == "5":
            phone = input("Enter phone number to search: ")
            results = search_by_phone(contacts, phone)
            print_contacts(results)

        elif choice == "6":
            location = input("Enter city or state to search: ")
            results = search_by_city_or_state(contacts, location)
            print_contacts(results)

        elif choice == "7":
            phone = input("Enter phone number to delete: ")
            if delete_by_phone(contacts, phone):
                print("Entry deleted successfully!")
            else:
                print("No entry found with that phone number.")

        elif choice == "8":
            phone = input("Enter phone number to update: ")
            first_name = input("Enter new first name: ")
            last_name = input("Enter new last name: ")
            city = input("Enter new city: ")
            state = input("Enter new state: ")
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

class TestPhonebook(unittest.TestCase):
    def test_add_entry(self):
        contacts = []
        add_entry(contacts, "First name", "Last name", "12345", "Kyiv", "UK")
        self.assertEqual(len(contacts), 1)
        self.assertEqual(contacts[0]["first_name"], "First name")

    def test_search_by_first_name(self):
        contacts = []
        add_entry(contacts, "First name", "Last name", "12345", "Kyiv", "UK")
        results = search_by_first_name(contacts, "First name")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["phone"], "12345")

    def test_delete_by_phone(self):
        contacts = []
        add_entry(contacts, "First name", "Last name", "12345", "Kyiv", "UK")
        deleted = delete_by_phone(contacts, "12345")
        self.assertTrue(deleted)
        self.assertEqual(len(contacts), 0)

if __name__ == "__main__":
    unittest.main(verbosity=2)