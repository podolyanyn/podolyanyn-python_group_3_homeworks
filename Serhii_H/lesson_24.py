# Task 1
# Write a program that reads in a sequence of characters and prints them in reverse order,
# using your implementation of Stack.

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

text = "minus 1,000,000 moscovites – beautiful!"

stack = Stack()

for word in text.split():
    stack.push(word)

print(text)

while not stack.is_empty():
    print(stack.pop(), end = " ")

print()
print('-' * 100)

# Task 2
# Write a program that reads in a sequence of characters,
# and determines whether it's parentheses, braces, and curly brackets are "balanced."

text = ("through selection, [moscovia] has produced terrible (moral) degenerates "
        "(whose concepts of Good and Evil are inverted) "
        "{throughout its history, this nation sits in shit "
        "(and yet wants to drag the whole world into it)}.")

stack2 = Stack()
pairs = {')': '(',
         '}': '{',
         ']': '['}

for i in text:
    if i in "({[":
        stack.push(i)
    elif i in ")}]":
        top = stack.pop()
        if top != pairs[i]:
            print("Not balanced")
            break
else:
    if stack.is_empty():
        print("Balanced")
    else:
        print("Not balanced")

print('-' * 100)


# Task 3
# Extend the Stack to include a method called get_from_stack
# that searches and returns an element e from a stack.
# Any other element must remain on the stack respecting their order.
# Consider the case in which the element is not found - raise ValueError with proper info Message

class StackWithGet(Stack):
    def get_from_stack(self, e):
        temp = []

        while not self.is_empty():
            item = self.pop()
            if item == e:
                break
            temp.append(item)
        else:
            while temp:
                self.push(temp.pop())
            raise ValueError(f"Element {e} not found in stack")

        while temp:
            self.push(temp.pop())

        return e

stack = StackWithGet()
stack.push('putin')
stack.push('is')
stack.push('hu.lo')
print(stack.get_from_stack('is'))
print(stack.items)
print('-' * 100)


# Extend the Queue to include a method called get_from_stack
# that searches and returns an element e from a queue
# Any other element must remain in the queue respecting their order.
# Consider the case in which the element is not found - raise ValueError with proper info Message

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0

    def get_from_queue(self, e):
        n = len(self.items)

        for i in range(n):
            item = self.dequeue()
            if item == e:
                return e
            self.enqueue(item)
        else:
            raise ValueError(f"Element {e} not found in queue")

queue = Queue()
queue.enqueue('lavrov')
queue.enqueue('is')
queue.enqueue('hu.lo')
queue.enqueue('too')
print(queue.get_from_queue('too'))
print(queue.items)