class UnsortedList:
    def __init__(self):
        self._data = []

    def __repr__(self):
        return repr(self._data)

    def append(self, item):
        self._data.append(item)

    def index(self, item):
        for i, val in enumerate(self._data):
            if val == item:
                return i
        raise ValueError(f"{item} не знайдено у списку")

    def pop(self, i=None):
        if i is None:
            return self._data.pop()
        if i < 0 or i >= len(self._data):
            raise IndexError("Невірний індекс")
        return self._data.pop(i)

    def insert(self, i, item):
        """Вставляє item на позицію i."""
        if i < 0 or i > len(self._data):
            raise IndexError("Невірний індекс для вставки")
        self._data.insert(i, item)

    def slice(self, start, stop):
        if start < 0 or stop > len(self._data) or start > stop:
            raise IndexError("Неправильні межі зрізу")
        new_list = UnsortedList()
        new_list._data = self._data[start:stop]
        return new_list

shopping_list = UnsortedList()

shopping_list.append("хліб")
shopping_list.append("молоко")
shopping_list.append("яйця")
shopping_list.append("сир")
print("Список покупок:", shopping_list)

print("Індекс 'яйця':", shopping_list.index("яйця"))

shopping_list.insert(1, "шоколад")
print("Після insert:", shopping_list)

print("Видалили (pop):", shopping_list.pop())
print("Список тепер:", shopping_list)

print("slice(1,3):", shopping_list.slice(1, 3))