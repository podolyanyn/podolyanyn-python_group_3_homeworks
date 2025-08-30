# Реалізуйте методи append, index, pop, insert для UnsortedList.
# Також реалізуйте метод зрізу, який отримує два параметри 'start' і 'stop'
# і повертає копію списку, починаючи з позиції і доходячи до позиції зупинки, але не включаючи її.

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None

    def add(self, item):
        if self.head == None:
            self.head = Node(item)
        else:
            current = Node(item)
            current.next = self.head
            self.head = current

    def __str__(self):
        result = ""
        current = self.head     # вказівник на поточний елемент списку
        while current:
            result += str(current.value) + ' > '
            current = current.next
        return result

    def search(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def size(self):
        current = self.head
        count = 0
        while current:
            current = current.next
            count += 1
        return count

    def search_all(self, value):
        """пошук елемента списку за значенням -
        якщо якесь значення зустрічається кілька раз, повертати всі значення;
        також повертати індекси елементів"""
        current = self.head
        index = 0
        new_list = []
        # Переходимо в циклі по всім елементам списку
        while current:
            # Якщо значення елементу дорівнює шуканому, зберігаємо в новий список кортеж (індексу та значення)
            if current.value == value:
                new_list.append((index, current.value))
            current = current.next
            index += 1
        return new_list

    def remove(self, value):
        current = self.head
        prev = None             # вказівник на попередній елемент списку
        if value == self.head.value:
            self.head = self.head.next
        else:
            # Переходимо в циклі поки значення елементу не стане дорівнювати шуканому:
            while current:
                if current.value == value:
                    # Якщо потрібний елемент знайдено - # зв'язуємо попередній елемент списку з наступним (який тепер current)
                    prev.next = current.next
                    break
                else:
                    prev = current
                    current = current.next

    def append(self, value):
        current = self.head
        if current == None:
            self.head = Node(value)
        else:
            # Переходимо в циклі до кінця списку (поки вказівник next останнього елементу не стане None)
            while current.next != None:
                current = current.next
            # створюємо новий елемент із заданим значенням value і змінюємо вказівник next останнього елементу на цей новий елемент
            current.next = Node(value)

    def pop(self):
        current = self.head
        prev = None
        if current.next == None:
            self.head = None
            return current.value
        else:
            # Переходимо в циклі до кінця списку (поки вказівник next останнього елементу не стане None)
            while current.next != None:
                prev = current      # при кожній ітерації також змінюємо вказівник на попередній елемент списку
                current = current.next
        prev.next = None
        return current.value

    def index(self, value):
        current = self.head
        index = 0
        # Шукаємо в циклі елемент списку з шуканим значенням, рахуючи індекс
        while current:
            if current.value == value:
                return index
            current = current.next
            index += 1

    def peek(self):
        current = self.head
        if current.next == None:
            return current.value
        else:
            # Переходимо в циклі до кінця списку (поки вказівник next останнього елементу не стане None)
            while current.next != None:
                current = current.next
        return current.value

    def insert(self, index, value):
        current = self.head
        prev = None
        count = 0
        if index == 0:
            self.head = Node(value)
            self.head.next = current
            return
        else:
            # Переходимо в циклі до потрібного індексу
            while count < index:
                prev = current  # при кожній ітерації також змінюємо вказівник на попередній елемент списку
                current = current.next
                count += 1
            # створюємо новий елемент із заданим значенням value і змінюємо вказівник next попереднього елементу на цей новий елемент
            prev.next = Node(value)
            prev.next.next = current    # зв'язуємо новий елемент списку з наступним (який тепер current)

    def slice(self, start, stop):
        current = self.head
        index = 0
        new_list = []
        while index < stop:
            # Якщо поточний індекс лежить в заданих межах від start до stop(не включаючи) - зберігаємо значення елементу в новий список
            if start <= index and stop > index:
                new_list.append(current.value)
            current = current.next
            index += 1
        return new_list

# Використання:
if __name__ == '__main__':
    a = linkedlist()
    a.add(1)
    a.add(2)
    a.add(3)
    a.add(4)
    a.add(5)
    a.add(6)
    a.add(4)
    print(f"{a.__str__()}")
    # Додавання нового елементу в кінець списку:
    a.append(8)
    print(f"after 'a.append(8)': \n{a.__str__()}\n")
    # Пошук потрібного значення в списку:
    print(f"a.search(5) - {a.search(5)}")   # True
    print(f"a.search(18) - {a.search(18)}") # False
    # Видалення елементу з заданим значенням:
    a.remove(2)
    print(f"after 'a.remove(2)': \n{a.__str__()}\n")
    # Пошук всіх входжень потрібного значення в список (з вказанням індексу входження):
    print(f"Всі входження числа 4 (індекс, значення): \n{a.search_all(4)}")
    # Вилучення елементу з кінця списку:
    print(f"a.pop = {a.pop()}")
    print(f"after a.pop: \n{a.__str__()}")
    # Пошук індексу входження в список потрібного значення:
    print(f"'a.index(5)': {a.index(5)}\n")
    # Додавання елементу в список за зазначеним індексом:
    a.insert(3, 33)
    print(f"after 'a.insert(index = 3, value = 33)': \n{a.__str__()}\n")
    # Повернення копії списку, реалізуя метод зрізу:
    print(f"a.slice[3, 6] = {a.slice(3, 6)}")