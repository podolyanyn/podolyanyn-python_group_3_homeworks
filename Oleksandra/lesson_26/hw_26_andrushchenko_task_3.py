class HashTable:
    def __init__(self, size=10):

        self.size = size
        self.table = [[] for _ in range(self.size)]
        self._length = 0

    def _hash(self, key):

        return hash(key) % self.size

    def __setitem__(self, key, value):

        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value  # Оновлення значення
                return
        self.table[index].append([key, value])  # Додавання нової пари
        self._length += 1

    def __getitem__(self, key):

        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        raise KeyError(f"Ключ '{key}' не знайдено")

    def __delitem__(self, key):

        index = self._hash(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][i]
                self._length -= 1
                return
        raise KeyError(f"Ключ '{key}' не знайдено")

    def __len__(self):

        return self._length

    def __contains__(self, key):

        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return True
        return False


# --- Тестування ---
if __name__ == "__main__":
    ht = HashTable()

    # Додаємо елементи
    ht['apple'] = 10
    ht['banana'] = 20
    ht['orange'] = 30
    ht['grape'] = 40

    print("--- Перевірка len() ---")
    print(f"Кількість елементів: {len(ht)}")  # Використовує __len__

    print("\n--- Перевірка in ---")
    print(f"'apple' in ht: {'apple' in ht}")  # Використовує __contains__
    print(f"'kiwi' in ht: {'kiwi' in ht}")  # Використовує __contains__

    print("\n--- Видалення елемента ---")
    del ht['banana']
    print(f"Кількість елементів після видалення: {len(ht)}")
    print(f"'banana' in ht: {'banana' in ht}")

    print("\n--- Доступ до елементів ---")
    try:
        print(f"Значення для 'orange': {ht['orange']}")
        print(f"Значення для 'banana': {ht['banana']}")
    except KeyError as e:
        print(e)
