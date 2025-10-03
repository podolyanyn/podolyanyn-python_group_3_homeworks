class FancyCollection:
    def __init__(self, items):
        self._items = list(items)
        print(f"Створено FancyCollection з {len(self._items)} елементів")

    def __getitem__(self, key):
        if isinstance(key, slice):
            print(f"Отримуємо зріз: {key.start}:{key.stop}:{key.step}")
            return FancyCollection(self._items[key])
        elif isinstance(key, int):
            print(f"Отримуємо елемент за індексом: {key}")
            return self._items[key]
        else:
            raise TypeError("Індекс має бути int або slice")

    def __iter__(self):
        return FancyIterator(self._items)

class FancyIterator:
    def __init__(self, items):
        self._items = items
        self._pos = 0
        print("FancyIterator створено")

    def __next__(self):
        if self._pos >= len(self._items):
            print("Ітерація завершена")
            raise StopIteration
        item = self._items[self._pos]
        print(f"Повертаємо елемент {self._pos}: {item}")
        self._pos += 1
        return item

if __name__ == "__main__":
    coll = FancyCollection(['Кіт', 'Пес', 'Змія', 'Голуб'])

    print("\nІтерація по колекції:")
    for el in coll:
        pass

    print("\nОтримання елементу за індексом 2:")
    print(coll[2])

    print("\nОтримання зрізу [1:3]:")
    sub_coll = coll[1:3]
    print(list(sub_coll))