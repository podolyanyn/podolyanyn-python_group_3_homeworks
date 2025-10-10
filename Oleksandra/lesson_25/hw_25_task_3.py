class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:

    def __init__(self):
        self.front = None  # Початок черги
        self.rear = None   # Кінець черги
        self.size = 0

    def is_empty(self):

        return self.front is None

    def enqueue(self, item):

        new_node = Node(item)
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1

    def dequeue(self):

        if self.is_empty():
            raise IndexError("Queue is empty - cannot dequeue.")

        dequeued_item = self.front.data
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        self.size -= 1
        return dequeued_item

    def peek(self):

        if self.is_empty():
            raise IndexError("Queue is empty - cannot peek.")
        return self.front.data

    def get_size(self):

        return self.size

    def __str__(self):

        items = []
        current = self.front
        while current:
            items.append(str(current.data))
            current = current.next
        return "Front -> " + " <- ".join(items) + " <- Rear"


# --- Приклад використання ---
if __name__ == "__main__":
    my_queue = Queue()

    print("Черга порожня?", my_queue.is_empty())

    print("\nДодаємо елементи до черги:")
    my_queue.enqueue(10)
    my_queue.enqueue(20)
    my_queue.enqueue(30)

    print("Вміст черги:", my_queue)
    print("Розмір черги:", my_queue.get_size())

    print("\nЕлемент на початку черги (peek):", my_queue.peek())

    print("\nВидаляємо елементи з черги:")
    while not my_queue.is_empty():
        print("Видалений елемент:", my_queue.dequeue())
        print("Поточна черга:", my_queue)

    print("\nЧерга порожня?", my_queue.is_empty())
    print("Розмір черги:", my_queue.get_size())

    # Перевірка помилок
    try:
        my_queue.dequeue()
    except IndexError as e:
        print("\nПомилка при dequeue:", e)

    try:
        my_queue.peek()
    except IndexError as e:
        print("Помилка при peek:", e)