#======================================================== 1 ============================================================
'''Task 1

Write a program that reads in a sequence of characters and prints them in reverse order, using your implementation of Stack.'''

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def is_empty(self):
        return self.stack == []  # return len(self.stack) == 0

    def size(self):
        return len(self.stack)

test_str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
chars_stack = Stack()
for char in test_str:
    chars_stack.push(char)

while not chars_stack.is_empty():
    print(chars_stack.pop(), end=' -> ')

#======================================================== 2 ============================================================
'''Task 2

Write a program that reads in a sequence of characters, and determines whether it's parentheses, braces, and curly brackets are "balanced."'''

def are_bracers_balanced(string_sequence):
    check_bracers_stack = Stack()
    test_dict = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for char in string_sequence:
        print(f'char = {char}')
        if char in '({[':
            check_bracers_stack.push(char)
        elif char in ')}]':
            if not check_bracers_stack.is_empty() and check_bracers_stack.peek() == test_dict[char]:
                check_bracers_stack.pop()
            else:
                 return False
    if not check_bracers_stack.is_empty():
        return False

    return True

# TESTING >>>
print(are_bracers_balanced(input('Pls enter a string with bracer fo check: ')))

#======================================================== 3 stack ============================================================
'''Task 3

Extend the Stack to include a method called get_from_stack that searches and returns an element e from a stack. Any other element must remain on the stack respecting their order. Consider the case in which the element is not found - raise ValueError with proper info Message'''
class EnhancedStack(Stack):
    def __init__(self):
        super().__init__()

    def get_from_stack(self, element):
        reserve_stack = Stack()
        result = None
        while not self.is_empty():
            if element == self.peek():
                result = self.pop()
                break
            else:
                reserve_stack.push(self.pop())

        # recovering initial stack either we found element or not
        while not reserve_stack.is_empty():
            self.push(reserve_stack.pop())


        if result is None:
            raise ValueError('No such element in stack')

        return result
#======================================================== 3 queue ============================================================
'''Task 3

Extend the Queue to include a method called get_from_stack that searches and returns an element e from a queue. 
Any other element must remain in the queue respecting their order. Consider the case in which the element is not found - raise ValueError with proper info Message'''
class Queue:
    def __init__(self):
        self._items = []

    def is_empty(self):
        return len(self._items) == 0

    def enqueue(self, item):
        self._items.append(item)  # швидко додаємо в кінець

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        return self._items.pop(0)  # забираємо з початку

    def peek(self):
        if self.is_empty():
            return None
        return self._items[0]

    def size(self):
        return len(self._items)

    def __repr__(self):
        representation = "<Queue>\n"
        for ind, item in enumerate(self._items, 1):
            representation += f"{ind}: {str(item)}\n"
        return representation

    def __str__(self):
        return self.__repr__()

class EnhancedQueue(Queue):

    def get_from_queue(self, element):
        reserve_queue = Queue()
        result = None

        while not self.is_empty():
            if result is None and element == self.peek():
                result = self.dequeue()
            else:
                reserve_queue.enqueue(self.dequeue())

        self._items = reserve_queue._items

        if result is None:
            raise ValueError('Element not found')

        return result


