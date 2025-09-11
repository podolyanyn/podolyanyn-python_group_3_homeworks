#Task 1
#Write a program that reads in a sequence of characters and prints them in reverse order,
# using your implementation of Stack.

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("pop from empty stack")

    def is_empty(self):
        return len(self.items) == 0

def reverse_sequence():
    stack = Stack()
    sequence = input("Input some sequence: ").strip()

    for char in sequence:
        stack.push(char)

    reversed_sequence = ""
    while not stack.is_empty():
        reversed_sequence += stack.pop()

    print("In reverse direction:", reversed_sequence)

if __name__ == "__main__":
    reverse_sequence()
################################################################################################
#Task 2
#Write a program that reads in a sequence of characters, and determines whether it's parentheses,
# braces, and curly brackets are "balanced."

class BracesStack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]

def is_balanced(sequence):
    stack = BracesStack()
    opening = "({["
    closing = ")}]"
    matches = {')': '(', '}': '{', ']': '['}

    try:
        has_brackets = False

        for char in sequence:
            if char in opening or char in closing:
                has_brackets = True

            if char in opening:
                stack.push(char)
            elif char in closing:
                if stack.is_empty() or stack.pop() != matches[char]:
                    return False

        if not has_brackets:
            print("У рядку немає жодної дужки.")

        return stack.is_empty()

    except Exception as e:
        print("Помилка:", str(e))
        return False

if __name__ == "__main__":
    text = input("Input sequence of symbols: ")
    if is_balanced(text):
        print("Дужки збалансовані.")
    else:
        print("Дужки НЕ збалансовані.")

##################################################################

#Task 3

#Extend the Stack to include a method called get_from_stack that searches and returns an element e from a stack.
# Any other element must remain on the stack respecting their order. Consider the case in which the element is not found
# - raise ValueError with proper info Message.
#Extend the Queue to include a method called get_from_stack that searches and returns an element e from a queue.
# Any other element must remain in the queue respecting their order. Consider the case in which the element is not found
# - raise ValueError with proper info Message.

class ExtendStack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def get_from_stack(self, e):
        temp_stack = []
        found = False


        while not self.is_empty():
            item = self.pop()
            if item == e:
                found = True
                break
            temp_stack.append(item)


        while temp_stack:
            self.push(temp_stack.pop())

        if not found:
            raise ValueError(f"Елемент '{e}' не знайдено в стеку.")

        return e

stack = ExtendStack()
stack.push("a")
stack.push("b")
stack.push("c")

print("До пошуку:", stack.items)

try:
    result = stack.get_from_stack("b")
    print("Знайдено:", result)
except ValueError as e:
    print("Помилка:", e)

print("Після пошуку:", stack.items)

class ExtendQueue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0

    def get_from_queue(self, e):
        temp_queue = []
        found = False

        # Витягуємо елементи, шукаючи e
        while not self.is_empty():
            item = self.dequeue()
            if item == e:
                found = True
                break
            temp_queue.append(item)

        # Повертаємо назад усі елементи
        for item in temp_queue:
            self.enqueue(item)

        if not found:
            raise ValueError(f"Елемент '{e}' не знайдено в черзі.")

        return e

queue = ExtendQueue()
queue.enqueue("x")
queue.enqueue("y")
queue.enqueue("z")

print("До пошуку:", queue.items)

try:
    result = queue.get_from_queue("y")
    print("Знайдено:", result)
except ValueError as e:
    print("Помилка:", e)

print("Після пошуку:", queue.items)

