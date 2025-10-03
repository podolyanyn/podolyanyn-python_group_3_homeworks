class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Stack:
    def __init__(self):
        self._top = None
        self._size = 0

    def push(self, item):
        self._top = Node(item, self._top)
        self._size += 1

    def pop(self):
        if self._top is None:
            raise IndexError("pop from empty stack")
        node = self._top
        self._top = node.next
        self._size -= 1
        return node.data

    def peek(self):
        if self._top is None:
            raise IndexError("peek from empty stack")
        return self._top.data

    def is_empty(self):
        return self._top is None

    def __len__(self):
        return self._size

    def __repr__(self):
        items = []
        cur = self._top
        while cur:
            items.append(repr(cur.data))
            cur = cur.next
        return "Stack[top: " + ", ".join(items) + "]"

    def get_from_stack(self, target):
        prev, cur = None, self._top
        while cur:
            if cur.data == target:
                if prev is None:
                    self._top = cur.next
                else:
                    prev.next = cur.next
                self._size -= 1
                return target
            prev, cur = cur, cur.next
        raise ValueError(f"Element {target!r} not found in stack")

class Queue:
    def __init__(self):
        self._head = None   # звідси дістаємо
        self._tail = None   # сюди додаємо
        self._size = 0

    def enqueue(self, item):
        node = Node(item)
        if self._tail is None:
            self._head = self._tail = node
        else:
            self._tail.next = node
            self._tail = node
        self._size += 1

    def dequeue(self):
        if self._head is None:
            raise IndexError("dequeue from empty queue")
        node = self._head
        self._head = node.next
        if self._head is None:
            self._tail = None
        self._size -= 1
        return node.data

    def peek(self):
        if self._head is None:
            raise IndexError("peek from empty queue")
        return self._head.data

    def is_empty(self):
        return self._head is None

    def __len__(self):
        return self._size

    def __repr__(self):
        items = []
        cur = self._head
        while cur:
            items.append(repr(cur.data))
            cur = cur.next
        return "Queue[front: " + ", ".join(items) + " :rear]"

    def get_from_queue(self, target):
        prev, cur = None, self._head
        while cur:
            if cur.data == target:
                if prev is None:
                    self._head = cur.next
                else:
                    prev.next = cur.next
                if cur is self._tail:
                    self._tail = prev
                self._size -= 1
                return target
            prev, cur = cur, cur.next
        raise ValueError(f"Element {target!r} not found in queue")

    def get_from_stack(self, target):
        return self.get_from_queue(target)

if __name__ == "__main__":
    s = Stack()
    for v in [1, 2, 3, 2, 4]:
        s.push(v)
    print(s)
    print(s.get_from_stack(2))
    print(s)

    q = Queue()
    for v in ["A", "B", "C", "B", "D"]:
        q.enqueue(v)
    print(q)                              
    print(q.get_from_queue("B"))
    print(q)