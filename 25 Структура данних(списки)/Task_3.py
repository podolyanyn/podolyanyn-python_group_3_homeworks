class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return f"Node({self.data})"


class Queue:
    def __init__(self):
        self._head = None
        self._tail = None
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

    def clear(self):
        cur = self._head
        while cur:
            nxt = cur.next
            cur.next = None
            cur = nxt
        self._head = self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def __iter__(self):
        cur = self._head
        while cur:
            yield cur.data
            cur = cur.next

    def __repr__(self):
        items = ", ".join(repr(x) for x in self)
        return f"Queue[front: {items} :rear]"

q = Queue()
q.enqueue("A"); q.enqueue("B"); q.enqueue("C")
print(q.peek())
print(q.dequeue())
print(len(q))
print(q)