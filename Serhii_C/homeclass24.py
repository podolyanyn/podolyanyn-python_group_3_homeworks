# Task
# 1
#
# Write
# a
# program
# that
# reads in a
# sequence
# of
# characters and prints
# them in reverse
# order, using
# your
# implementation
# of
# Stack.

# class Stack():
#     def __init__(self,list):
#         self.list = list
#
#     def push(self,item):
#         self.list.append(item)
#         print(self.list)
#     def pop(self):
#         return self.list.pop()
#     def reverse(self):
#         self.list2 = []
#         n = len(self.list)-1
#         for i in self.list:
#             self.list2.append(self.list[n])
#             n -= 1
#         return self.list2
#
#
#
# a = Stack([1,2,3])
#
# a.push(4)
#
# print(a.reverse())

# Завдання 2
#
# Напишіть програму, яка зчитує послідовність символів та визначає, чи є її дужки, фігурні дужки та фігурні дужки «збалансованими».

# def balanced(string):
#     a = string.count('(')
#     b = string.count(')')
#     c = string.count('[')
#     d = string.count(']')
#     e = string.count('{')
#     f = string.count('}')
#     flag1 = False
#     flag2 = False
#     flag3 = False
#     if a==b or a==0 and b==0:
#         flag1 = True
#     else:
#         print(f'()are not balanced , symbol ( have quantity {a} and symbol ) have quantity {b}')
#     if c==d or c==0 and d==0:
#         flag2 = True
#     else:
#         print(f'[] are not balanced , symbol [ have quantity {c} and symbol ] have quantity {d}')
#
#     if e==f or e==0 and f==0:
#         flag3 = True
#     else:
#         print(f'Symbols "Фігурні дужки " are not balanced ')
#
#     if flag1 == True and flag2== True and flag3== True:
#         print('Рядок є збалансований')
#
# # balanced('((((())))))){}{]]')
# balanced('(k)()q[g]e[]1245')
# Завдання 3
#
# Розширте стек, включивши метод під назвою get_from_stack, який шукає та повертає елемент e зі стеку.
# Будь-який інший елемент повинен залишатися в стеку, дотримуючись їхнього порядку. Розглянемо випадок,
# коли елемент не знайдено - викличіть ValueError з належною інформацією Message.

# class Stack():
#     def __init__(self,list):
#         self.list = list
#
#     def push(self,item):
#         self.list.append(item)
#         print(self.list)
#     def pop(self):
#         return self.list.pop()
#     def reverse(self):
#         self.list2 = []
#         n = len(self.list)-1
#         for i in self.list:
#             self.list2.append(self.list[n])
#             n -= 1
#         return self.list2
#
#     def get_from_stack(self,e):
#         b = False
#         n = len(self.list) - 1
#         for i in range(len(self.list)):
#             if self.list[n] == e:
#                 self.list.pop(n)
#                 b= True
#
#
#             else:
#                 n -= 1
#         if b == False:
#             raise ValueError(f'Введеного вами символа {e} немає в рядку')
#
#         return self.list
#
#
#
#
# b = Stack([1,2,3,4,5])
# b.push('a')
# # print(b.reverse())
# print(b.get_from_stack(2))
# print(b.get_from_stack(4))
# print(b.get_from_stack(85))

# Розширте Чергу, включивши метод під назвою get_from_stack, який шукає та повертає елемент e з черги.
# Будь-який інший елемент повинен залишатися в черзі, дотримуючись їхнього порядку. Розглянемо випадок,
# коли елемент не знайдено - викличіть ValueError з належною інформацією Message.
# import random
#
# class Queue:
#     def __init__(self):
#         self.queue = [random.randint(0,20) for i in range(10)]
#
#
#     def enqueue(self,item):
#         self.queue.append(item)
#
#     def dequeue(self):
#         if len(self.queue) <1:
#             return None
#         return self.queue.pop(0)
#
#     def size(self):
#         return len(self.queue)
#
#     def isEmpty(self):
#         return len(self.queue) == 0
#
#     def __str__(self):
#         return str(self.queue)
#
#     def get_from_queue(self,e):
#         b = False
#         n = 0
#         for i in range(len(self.queue)):
#             if self.queue[n] == e:
#                 self.queue.pop(n)
#                 b= True
#
#
#             else:
#                 n += 1
#         if b == False:
#             raise ValueError(f'Введеного вами символа {e} немає в рядку')
#
#         return self.queue
#
# a = Queue()
# print(a)
# print(a.get_from_queue(5))


