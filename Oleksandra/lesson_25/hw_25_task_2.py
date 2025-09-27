class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:

    def __init__(self):
        self.top = None
        self.size = 0

    def is_empty(self):

        return self.top is None

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty - cannot pop.")
        popped_item = self.top.data
        self.top = self.top.next
        self.size -= 1
        return popped_item

    def peek(self):

        if self.is_empty():
            raise IndexError("Stack is empty - cannot peek.")
        return self.top.data

    def get_size(self):

        return self.size

    def __str__(self):
        """Вивести стек у вигляді рядка."""
        items = []
        current = self.top
        while current:
            items.append(str(current.data))
            current = current.next
        return "Top -> " + " -> ".join(items)

# --- Тестування ---
if __name__ == "__main__":
    my_stack = Stack()

    print("Стек порожній?", my_stack.is_empty())

    print("\nДодаємо елементи: 10, 20, 30")
    my_stack.push(10)
    my_stack.push(20)
    my_stack.push(30)
    print("Вміст стеку:", my_stack)
    print("Розмір стеку:", my_stack.get_size())

    print("\nPeek (верхній елемент):", my_stack.peek())

    print("\nВидаляємо елементи зі стеку:")
    while not my_stack.is_empty():
        print("Видалений елемент:", my_stack.pop())
        print("Поточний стек:", my_stack)

    print("\nСтек порожній?", my_stack.is_empty())
    print("Розмір стеку:", my_stack.get_size())

    # Перевірка помилок
    try:
        my_stack.pop()
    except IndexError as e:
        print("Помилка при pop:", e)

    try:
        my_stack.peek()
    except IndexError as e:
        print("Помилка при peek:", e)