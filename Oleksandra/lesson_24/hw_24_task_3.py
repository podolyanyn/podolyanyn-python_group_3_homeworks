# Реалізація класу Stack
class Stack:
    def __init__(self):
        self._items = []

    def is_empty(self):
        return not self._items

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop з порожнього стека")
        return self._items.pop()

    def get_from_stack(self, element):

        temp_stack = Stack()
        found_element = None

        # Пошук потрібного елемента
        while not self.is_empty():
            current_item = self.pop()
            if current_item == element:
                found_element = current_item
                break
            temp_stack.push(current_item)

        # Відновлення порядку елементів
        while not temp_stack.is_empty():
            self.push(temp_stack.pop())

        if found_element is None:
            raise ValueError(f"Елемент '{element}' не знайдено у стеку.")

        return found_element

    def __str__(self):
        return f"Стек (верх -> низ): {list(reversed(self._items))}"


# Реалізація класу Queue
class Queue:
    def __init__(self):
        self._items = []

    def is_empty(self):
        return not self._items

    def enqueue(self, item):
        self._items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue з порожньої черги")
        return self._items.pop(0)

    def get_from_queue(self, element):

        temp_list = []
        found_element = None

        while not self.is_empty():
            current_item = self.dequeue()
            if current_item == element and found_element is None:
                found_element = current_item  # Знайшли потрібний елемент
            else:
                temp_list.append(current_item)  # Інші елементи зберігаємо

        # Відновлення черги у початковому порядку
        for item in temp_list:
            self.enqueue(item)

        if found_element is None:
            raise ValueError(f"Елемент '{element}' не знайдено у черзі.")

        return found_element

    def __str__(self):
        return f"Черга (front -> back): {self._items}"


# --- Приклад використання ---
if __name__ == "__main__":
    print("--- Тестування Stack ---")
    my_stack = Stack()
    my_stack.push(10)
    my_stack.push(20)
    my_stack.push(30)
    my_stack.push(40)
    print(f"Початковий {my_stack}")

    try:
        found = my_stack.get_from_stack(20)
        print(f"Знайдено елемент: {found}")
        print(f"Стек після пошуку: {my_stack}")

        # Спроба знайти неіснуючий елемент
        my_stack.get_from_stack(100)
    except ValueError as e:
        print(f"Помилка: {e}")

    print("\n--- Тестування Queue ---")
    my_queue = Queue()
    my_queue.enqueue("A")
    my_queue.enqueue("B")
    my_queue.enqueue("C")
    my_queue.enqueue("D")
    print(f"Початкова {my_queue}")

    try:
        found = my_queue.get_from_queue("C")
        print(f"Знайдено елемент: {found}")
        print(f"Черга після пошуку: {my_queue}")

        # Спроба знайти неіснуючий елемент
        my_queue.get_from_queue("Y")
    except ValueError as e:
        print(f"Помилка: {e}")