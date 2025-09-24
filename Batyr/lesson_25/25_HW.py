class Node:
    def __init__(self, data):
        self._data = data
        self._next = None

    def get_data(self):
        return self._data

    def get_next(self):
        return self._next

    def set_data(self, data):
        self._data = data

    def set_next(self, new_next):
        self._next = new_next
#======================================================= 1 =============================================================
"""Extend UnsortedList

Implement append, index, pop, insert methods for UnsortedList. Also implement a slice method, which will take
 two parameters 'start' and 'stop', and return a copy of the list starting at the position and going up to but not including the stop position."""

class UnsortedList:

    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self._head)
        self._head = temp

    def size(self):
        current = self._head
        count = 0
        while current is not None:
            count += 1
            current = current.get_next()

        return count

    def search(self, item):
        current = self._head
        found = False
        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()

        return found

    def remove(self, item):
        current = self._head
        previous = None
        found = False
        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()

        if previous is None:
            self._head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def __repr__(self):
        representation = "<UnsortedList: "
        current = self._head
        while current is not None:
            representation += f"{current.get_data()} "
            current = current.get_next()
        return representation + ">"


class ExtendedUnsortedList(UnsortedList):
    def append(self, data):
        if self._head is None:
            self.add(data)
        else:
            current = self._head
            while not current.get_next() is None:
                current = current.get_next()
            current.set_next(Node(data))

    def index(self, value):
        if self.is_empty():
            return None
        current = self._head
        index = 0


        while not current is None:
            if current.get_data() == value:
                return index
            current = current.get_next()
            index += 1
        return ValueError('No such element')

    def insert(self, pos, item):
        if (self.is_empty() and pos != 0) or pos < 0:
            raise IndexError


        if pos == 0:
            temp_node = Node(item)
            temp_node.set_next(self._head)
            self._head = temp_node
        else:
            current = self._head
            index = 0
            while not current is None:
                if index == pos - 1:
                    temp_node = Node(item)
                    temp_node.set_next(current.get_next())
                    current.set_next(temp_node)
                    return

                current = current.get_next()
                index += 1
        raise IndexError("Index out of range")

    def pop(self, pos):
        if self.is_empty() or pos < 0:
            raise IndexError


        if pos == 0:
            data = self._head.get_data()
            self._head = self._head.get_next()
            return data
        else:
            current = self._head
            index = 0
            while not current is None:
                if index == pos - 1:
                    data = current.get_next().get_data()
                    current.set_next(current.get_next().get_next())
                    return data
                current = current.get_next()
                index += 1

        raise IndexError("Index out of range")

#======================================================= 2 =============================================================
"""Task 2

Implement a stack using a singly linked list."""


class LinkedList(object):
    def __init__(self):
        self.head = None

    def add(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

    def __str__(self):
        result = ''
        current = self.head
        while current:
            result += str(current.data) + ' | '
            current = current.next
        return result


class Stack:
    def __init__(self):
        self.stack = LinkedList()
        self.nodes_number = 0

    def push(self, value):
        self.stack.add(value)
        self.nodes_number += 1

    def pop(self):
        if self.is_empty():
            return None
        data = self.stack.head.data
        self.stack.head = self.stack.head.next
        self.nodes_number -= 1
        return data

    def peek(self):
        if self.is_empty():
            return None
        return self.stack.head.data

    def is_empty(self):
        return self.stack.head is None

    def size(self):
        return self.nodes_number

#======================================================= 3 =============================================================
"""Task 3

Implement a queue using a singly linked list."""

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.nodes_number = 0

    def is_empty(self):
        return self.front is None

    def enqueue(self, item):
        new_node = Node(item)
        self.nodes_number += 1
        if self.size() == 0:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.set_next(new_node)
            self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            raise ValueError
        data = self.front.get_data()
        self.front = self.front.get_next()
        self.nodes_number -= 1
        if self.front is None:  # якщо черга порожня, rear теж None
            self.rear = None
        return data

    def size(self):
        return self.nodes_number

