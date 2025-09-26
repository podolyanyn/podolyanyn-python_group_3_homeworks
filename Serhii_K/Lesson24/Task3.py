# Task 3:
# 1) Розширити стек, додавши до нього метод get_from_stack, який шукає і повертає елемент e зі стеку.
# Всі інші елементи повинні залишатися у стеку з дотриманням їх порядку.
# Розглянемо випадок, коли елемент не знайдено - згенеруємо ValueError з відповідним інформаційним повідомленням Message

class My_Stack:
    def __init__(self):
        self.my_list = []

    def push(self, value):
        self.my_list.append(value)

    def pop(self):
        return self.my_list.pop()

    def peek(self):
        return self.my_list[-1]

    def size(self):
        return len(self.my_list)

    def empty(self):
        return len(self.my_list) == 0

    def get_from_stack(self, element):
        list1 = []
        OK = True
        x = None
        for i in range(len(self.my_list)):
            if self.my_list[-1] == element:       # Якщо верхній елемент стеку є шуканий елемент - зберігаємо його в зміннну Х
                x = self.my_list.pop()
                break
            else:
                list1.append(self.my_list.pop())  # інакше вилучаємо елемент стеку та зберігаємо в новому списку
        # Якщо пройдено весь стек до основи і потрібний елемент не знайдено, то OK = False
        if len(self.my_list) == 0 and x is None:
            OK = False
        # Повертаємо з нового списку всі вилучені елементи обратно в стек:
        for i in range(len(list1)):
            self.my_list.append(list1.pop())
        # Якщо елемент не знайдено - генеруємо помилку, інакше повертаємо шуканий елемент:
        if not OK:
            raise ValueError('Елемент не знайдено!')
        else:
            return x

# Використання:
st = My_Stack()
st.push(1)
st.push(2)
st.push(3)
st.push(4)
st.push(5)
print(f'Cтек: {st.my_list}')
print(f"Вилучений елемент стека: {st.get_from_stack(3)}")
print(f'Cтек: {st.my_list}')


# 2) Розширити чергу, додавши до неї метод get_from_stack, який шукає і повертає елемент e з черги.
# Всі інші елементи повинні залишатися у черзі з дотриманням їх порядку.
# Розглянемо випадок, коли елемент не знайдено - згенеруємо ValueError з відповідним інформаційним повідомленням Message

class MyQueue:
    def __init__(self):
        self.my_list = []

    def unqueue(self, data):
        self.my_list.insert(0,data)

    def dequeue(self):
        self.my_list.pop()

    def is_empty(self):
        return len(self.my_list) == 0

    def size(self):
        return len(self.my_list)

    def __str__(self):
        return [(i, d) for i, d in enumerate(self.my_list)]

    def get_from_stack(self, element):
        list1 = []
        OK = True
        x = None
        for i in range(len(self.my_list)):
            if self.my_list[-1] == element:  # Якщо верхній елемент черги є шуканий елемент - зберігаємо його в зміннну Х
                x = self.my_list.pop()
                break
            else:
                list1.append(self.my_list.pop())  # інакше вилучаємо елемент черги та зберігаємо в новому списку
        # Якщо пройдено всю чергу і потрібний елемент не знайдено, то OK = False
        if len(self.my_list) == 0 and x is None:
            OK = False
        # Повертаємо з нового списку всі вилучені елементи обратно в чергу:
        for i in range(len(list1)):
            self.my_list.append(list1.pop())
        # Якщо елемент не знайдено - генеруємо помилку, інакше повертаємо шуканий елемент:
        if not OK:
            raise ValueError('Елемент не знайдено!')
        else:
            return x

q = MyQueue()
q.unqueue(1)
q.unqueue(2)
q.unqueue(3)
q.unqueue(4)
q.unqueue(5)
print()
print(f'Черга: {q.my_list}')
print(f"Вилучений елемент черги: {q.get_from_stack(5)}")
print(f'Черга: {q.my_list}')