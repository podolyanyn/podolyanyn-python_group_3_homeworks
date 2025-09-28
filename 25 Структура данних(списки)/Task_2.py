class Node:
    def __init__(self, data, next_=None):
        self.data = data
        self.next = next_

    def __repr__(self):
        return f"Node({self.data})"


class Stack:
    def __init__(self):
        self._top = None   # верхній вузол
        self._size = 0     # кількість елементів

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

    def __iter__(self):
        current = self._top
        while current:
            yield current.data
            current = current.next

    def __repr__(self):
        items = ", ".join(repr(x) for x in self)
        return f"Stack[top: {items}]"

s = Stack()
print(s.is_empty())
s.push(10)
s.push(20)
s.push(30)

print(len(s))
print(s.peek())
print(s.pop())
print(s.pop())
print(s)
