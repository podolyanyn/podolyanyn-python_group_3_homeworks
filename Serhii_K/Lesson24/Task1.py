# Task 1:
# Напишіть програму, яка зчитує послідовність символів
# і виводить їх у зворотному порядку, використовуючи вашу реалізацію стеку.

# Моя реалізація стеку:
class My_Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)

    def empty(self):
        return len(self.stack) == 0

def reverse_simbols(simbols) -> list:
    """Функція, що спочатку зберігає елементи в стеку по порядку;
    а потім вилучає елементи зі стеку в обратному порядку"""
    stack1 = My_Stack()     # екземпляр стеку
    # збереження елементів в стек:
    for item in simbols:
        stack1.push(item)
    # вилучення елементів зі стеку в обратному порядку в новий список:
    reversed_simvols = []
    while not stack1.empty():
        reversed_simvols.append(stack1.pop())
    return reversed_simvols

# Використання:
my_string = "Рвал дед лавр"
new_list = reverse_simbols(my_string)
# об'єднання елементів списку в рядок:
print("".join(new_list))

list1 = ['100', 15, "кіт"]
print(reverse_simbols(list1))


