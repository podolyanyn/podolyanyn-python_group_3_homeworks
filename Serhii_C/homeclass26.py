# import random
# import time
#
# num_list = sorted([random.randint(1,200) for i in range(10000)])
# print(num_list)
#
#
# def binary_search(nums, target):
#    left = 0
#    right = len(nums) - 1
#    flag = False
#    while left <= right:
#        mid = (left + right) // 2
#        if nums[mid] == target:
#            flag = True
#            return f'Number {target} was found  with index {mid}'
#        elif nums[mid] > target:
#            right = mid - 1
#        elif nums[mid] < target:
#            left = mid + 1
#    if flag == False:
#        return f'Number {target} was not found in list'
#
#
# print(binary_search(num_list, 10))
#
#
# # num_list = sorted([random.randint(1, 20) for _ in range(100)])
# # print(num_list)
#
# def fibonacci_search(num, target):
#
#     n = len(num)
#     fib_2 = 0
#     fib_1 = 1
#     fib_m = fib_2 + fib_1
#
#     while fib_m < n:
#         fib_2 = fib_1
#         fib_1 = fib_m
#         fib_m = fib_2 + fib_1
#
#     move = -1
#
#     while fib_m > 1:
#         i = min(move + fib_2, n - 1)
#
#         if num[i] == target:
#             return f'Число {target} знайдено за індексом {i}'
#
#         elif num[i] < target:
#             fib_m = fib_1
#             fib_1 = fib_2
#             fib_2 = fib_m - fib_1
#             move = i
#
#         else:
#             fib_m = fib_2
#             fib_1 = fib_1 - fib_2
#             fib_2 = fib_m - fib_1
#
#     if fib_1 and num[move + 1] == target:
#         return f'Число {target} знайдено за індексом {move + 1}'
#
#     return f'Число {target} не знайдено у списку'
# time_start = time.time()
# print(fibonacci_search(num_list, 135))
# print(f'fibonacci has done task  in {time.time() - time_start} s')
# time_start = time.time()
# print(binary_search(num_list, 135))
# print(f'binary has done task  in {time.time() - time_start} s')

# рез-ти:
# fibonacci:3.0040740966796875e-05 s,2.8371810913085938e-05 s,1.6450881958007812e-05 s,3.528594970703125e-05
# binary:2.8133392333984375e-05 s,4.4345855712890625e-05 s,7.3909759521484375e-06 s,2.9802322387695312e-05
# Принципової різниці в швидкості немає, складність у обох логарифмічна