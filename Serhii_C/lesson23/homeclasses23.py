import random
import time
# first_list =[random.randint(0,100) for i in range(100000)]
# second_list = [random.randint(0,100) for i in range(100000)]
#
#
#
# def question1(first_list, second_list):
#     res = []
#     for el_first_list in first_list:
#         if el_first_list in second_list:
#             res.append(el_first_list)
#     return res
#
# time_start = time.time()
# question1(first_list, second_list)
# print(f'question1 in {time.time() - time_start} s')

# при довжині  списків по 10 елементів час склав question1 in 4.0531158447265625e-06 s
# при довжині  списків по 100 елементів  час склав question1 in question1 in 8.654594421386719e-05 s , більше у 21 раз ніж при 10
# при довжині  списків по 1000 елементів  час склав question1 in question1 in question1 in 0.0014073848724365234 s , більше у 16 раз
# при довжині  списків по 10000 елементів  час склав question1 in 0.0070836544036865234 s, більше у 5,33
# при довжині  списків по 10000 елементів  час склав question1 in 0.18964028358459473 s , більше у 26

# тобто як що брати до уваги час , то геть не логарифмічна залежність. Більше схоже на квадратичну ,
# тому що при довжині рядків по 3 треба буде 9 перевірок , а при довжині по 6 вже 36 перевірок.
# import sys
# sys.set_int_max_str_digits(0)
#
# def question2(n):
# 	for _ in range(10):
# 		n **= 3
#
# 	return n
# question2(10)
#
# time_start = time.time()
# print(question2(5))
# print(f'question2 in {time.time() - time_start} s')
# # При n=10 час question2 in 0.03794431686401367 s
# # При n=100 час question2 in 0.011343955993652344 s
# # При n=1000 час question2 in 0.020244598388671875 s
# #цей точно не є квадратичним як у умові завдання , алгоритм має постійну кількість операцій - 10 , а час залежить від числа n - і зростає
# # дуже повільно n збільшилося у 10 раз , а час лише у 2. Штучний інтелект підказує що це O(log(n))


# def question3(first_list, second_list):
#    temp = first_list
#    for el_second_list in second_list[:]:
#       flag = False
#       for check in temp:
#          if el_second_list == check:
#             flag = True
#             break
#       if not flag:
#          temp.append(second_list)
#    return temp
#
# # It is O(n**2)

# def question4(input_list: List[int]) -> int:
#   res: int = 0
#   for el in input_list:
#     if el > res:
#       res = el
#   return res

# It is O(n)

# def question5(n: int) -> List[Tuple[int, int]]:
#     res: List[Tuple[int, int]] = []
#     for i in range(n):
#         for j in range(n):
#             res.append((i, j))
#     return res
# IT is O(n**2) - because 2 cykles

# def question6(n: int) -> int:
#     while n > 1:
#         n /= 2
#     return n
# It is O(1) - just 1 step