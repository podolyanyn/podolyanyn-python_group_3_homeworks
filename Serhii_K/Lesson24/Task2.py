# Task 2:
# Напишіть програму, яка зчитує послідовність символів
# і визначає, чи є дужки, фігурні дужки та дужки "збалансованими".

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

def balanced(braces_string: str) -> bool:
    """Функція, спочатку знаходить в рядку пряму дужку і зберігає їх в стеку;
    а потім, коли знаходить відповідну їй зворотню дужку - вилучає її зі стеку;
    якщо в кінці в стеку залишаються дужки, або стек спустошується достроково - дужки не збалансовані"""
    my_stack = My_Stack()
    # Дужки для порівняння:
    str1 = "([{"
    str2 = ")]}"
    for char in braces_string:
        # Зберігаємо прямі дужки в стек:
        if char in str1:
            my_stack.push(char)
        # Якщо знаходимо обратну дужку - перевіряємо її чи співпадає вона з відповідною прямою дужкою з вершини стеку
        # (має значення якої саме форми дужки)
        elif char in str2:
            i = str2.find(char)     # індекс дужок з str2
            if my_stack.empty():    # Якщо стек пустий достроково - дужки не збалансовані (повертаємо False)
                return False
            else:
                ch = my_stack.pop() # Вилучаємо пряму дужку з вершини стеку
            if ch != str1[i]:       # Перевіряємо чи вона тієї ж форми, що і обратна дужка. Якщо ні - дужки не збалансовані (повертаємо False)
                return False
    # якщо після всіх кроків стек пустий - дужки збалансовані (повертаємо True)
    if my_stack.empty():
        return True
    else:
        return False

# Використання:
print(balanced("(1 + 1) * 2 + (15 -12)"))   # True
print(balanced("[[9] 15]"))                 # True
print(balanced("({}([()]()()))"))           # True
print(balanced("[[])]"))                    # False
print(balanced("({}([(]())()))"))           # False