class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.items:
            raise IndexError("Спроба зчитати  із порожнього стеку")
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def get_from_stack(self, e):
        if e not in self.items:
            raise ValueError(f"Елемент {e} не знайдено у стеку")

        new_items = []
        found = None
        for item in self.items:
            if item == e and found is None:
                found = item
                continue
            new_items.append(item)

        self.items = new_items
        return found


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.items:
            raise IndexError("Спроба з порожньої черги")
        return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0

    def get_from_stack(self, e):
        if e not in self.items:
            raise ValueError(f"Елемент {e} не знайдено у черзі")

        new_items = []
        found = None
        for item in self.items:
            if item == e and found is None:
                found = item
                continue
            new_items.append(item)

        self.items = new_items
        return found
s = Stack()
s.push(1)
s.push(2)
s.push(3)

print(s.get_from_stack(2))
print(s.items)

q = Queue()
q.enqueue("a")
q.enqueue("b")
q.enqueue("c")

print(q.get_from_stack("b"))
print(q.items)
