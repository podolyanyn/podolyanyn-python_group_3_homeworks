# Завдання 1
# Розширити UnsortedList
# Pеалізуйте методи append, index, pop, insert для UnsortedList. Також реалізуйте метод slice, який прийматиме
# два параметри 'start' і 'stop' і повертатиме копію списку, починаючи з позиції і закінчуючи
# позицією stop, але не включаючи її.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class UnsortedList:
    def __init__(self):
        self.head = None

    def append(self, item):
        node = Node(item)
        if not self.head:
            self.head = node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = node

    def index(self, item):
        cur, pos = self.head, 0
        while cur:
            if cur.data == item:
                return pos
            cur = cur.next
            pos += 1
        return -1

    def pop(self, pos=None):
        if not self.head:
            return None
        if pos == 0 or pos is None:
            cur = self.head
            if not cur.next:
                self.head = None
                return cur.data
            prev = None
            while cur.next:
                prev, cur = cur, cur.next
            if prev:
                prev.next = None
            return cur.data
        cur, prev, i = self.head, None, 0
        while cur and i < pos:
            prev, cur = cur, cur.next
            i += 1
        if not cur:
            return None
        prev.next = cur.next
        return cur.data

    def insert(self, pos, item):
        node = Node(item)
        if pos == 0:
            node.next = self.head
            self.head = node
            return
        cur, prev, i = self.head, None, 0
        while cur and i < pos:
            prev, cur = cur, cur.next
            i += 1
        if prev:
            prev.next = node
            node.next = cur

    def slice(self, start, stop):
        result = UnsortedList()
        cur, i = self.head, 0
        while cur and i < stop:
            if i >= start:
                result.append(cur.data)
            cur = cur.next
            i += 1
        return result

    def show(self):
        cur = self.head
        while cur:
            print(cur.data, end=' → ')
            cur = cur.next
        print('None')

# ul = UnsortedList()
# ul.append('A')
# ul.append('B')
# ul.append('C')
# ul.insert(1, 'X')     # A → X → B → C
# ul.show()
#
# print("Index of B:", ul.index('B'))
# print("Pop:", ul.pop())  # C
# ul.show()
#
# sliced = ul.slice(0, 2)
# sliced.show()             # A → X

########################################################################################################################
# Завдання 2
# Реалізуйте стек, використовуючи одноз'єднаний список.

class LinkedStack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, item):
        node = Node(item)
        node.next = self.top
        self.top = node

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        item = self.top.data
        self.top = self.top.next
        return item

    def peek(self):
        if self.is_empty():
            return None
        return self.top.data

    def show(self):
        cur = self.top
        while cur:
            print(cur.data, end=' → ')
            cur = cur.next
        print('None')

# s = LinkedStack()
# s.push('A')
# s.push('B')
# s.push('C')
# s.show()         # C → B → A → None
#
# print(s.pop())   # C
# s.show()         # B → A → None
#
# print(s.peek())  # B

########################################################################################################################
# запитання 3
# Реалізуйте чергу за допомогою одноз'єднаного списку.

class LinkedQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, item):
        node = Node(item)
        if self.rear:
            self.rear.next = node
        else:
            self.front = node
        self.rear = node

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        item = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return item

    def peek(self):
        if self.is_empty():
            return None
        return self.front.data

    def show(self):
        cur = self.front
        while cur:
            print(cur.data, end=' → ')
            cur = cur.next
        print('None')

# q = LinkedQueue()
# q.enqueue('A')
# q.enqueue('B')
# q.enqueue('C')
# q.show()         # A → B → C → None
#
# print(q.dequeue())  # A
# q.show()            # B → C → None
#
# print(q.peek())     # B
