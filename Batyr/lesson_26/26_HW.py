#=========================================================== 1 =========================================================
"""Реалізувати алгоритм бінарного пошуку за допомогою рекурсії."""
def search_binary_recursively(array, value, left, right):

    mid = (left + right)// 2

    if left > right:
        return -1

    if array[mid] > value:
        return search_binary_recursively(array, value, left, mid - 1)
    elif array[mid] < value:
        return search_binary_recursively(array, value, mid + 1, right)
    else:
        return mid

#=========================================================== 2 = за допомогою АІ =========================================================
"""Прочитати про Fibonacci search та імплементуйте його за допомогою Python. Визначте складність алгоритму та порівняйте його з бінарним пошуком"""

#================================ Моя версія знаходження потрібного числа фібоначчі і максимального потрібного числа фібоначі
# def get_fibonacci(k):
#     if k == 0:
#         return 0
#
#     if k == 1:
#         return 1
#
#     return get_fibonacci(k - 1) + get_fibonacci(k -2)
# #
# def get_max_fibonacci(arr_length):
#     i = 0
#     while True:
#         if get_fibonacci(i) <= arr_length < get_fibonacci(i + 1):
#             return i


# ========================== AI версія знаходження потрібного числа фібоначі як менш затратної і швидкої
#
def get_max_fibonacci(arr_length):
    a, b = 0, 1
    while b < arr_length:
        a, b = b, a + b
    return b

def get_fibonacci(k: int) -> int:
    if k == 0:
        return 0
    elif k == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, k + 1):
        a, b = b, a + b
    return b

def search_fibonacci(array, value, offset, max_fib):
    if max_fib == 0:
        return -1

    # Обчислюємо індекс для порівняння
    index = min(offset + get_fibonacci(max_fib - 2), len(array) - 1)

    if array[index] == value:
        return index
    elif array[index] < value:
        # Зсуваємо offset вперед
        return search_fibonacci(array, value, index, max_fib - 1)
    else:
        # offset залишається, але зменшуємо розмір
        return search_fibonacci(array, value, offset, max_fib - 2)



# TEST
arr = [10, 22, 35, 40, 45, 50, 80, 82, 85, 90, 100]
print(search_fibonacci(arr, 40, -1, get_max_fibonacci(len(arr))))