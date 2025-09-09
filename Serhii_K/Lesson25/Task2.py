# Task 2:
# Реалізувати стек з використанням однозв'язного списку.

from Task1 import Node, linkedlist

class My_Stack:
    def __init__(self):
        self.stack = linkedlist()

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack.peek()

    def size(self):
        return self.stack.size()

    def empty(self):
        return self.stack.size() == 0

    def __str__(self):
        return self.stack.__str__()

# Використання:
if __name__ == '__main__':
    stack = My_Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.__str__())

    print(f"stack size = {stack.size()}")
    print(f"stack.peek() = {stack.peek()}")

    print(stack.pop())  # 3
    print(stack.pop())  # 2
    print(stack.pop())  # 1

    print(f"stack size = {stack.size()}")
    print(f"stack.empty: {stack.empty()}")
