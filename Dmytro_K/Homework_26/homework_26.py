def binary_search(arr, target, left=0, right=None):
    if right is None:
        right = len(arr) - 1
    if left > right:
        return -1
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    if arr[mid] > target:
        return binary_search(arr, target, left, mid - 1)
    return binary_search(arr, target, mid + 1, right)

def fibonacci_search(arr, x):
    fib2, fib1 = 0, 1
    fib = fib1 + fib2
    while fib < len(arr):
        fib2, fib1 = fib1, fib
        fib = fib1 + fib2

    gap = -1
    while fib > 1:
        i = min(gap + fib2, len(arr) - 1)
        if arr[i] < x:
            fib = fib1
            fib1 = fib2
            fib2 = fib - fib1
            gap = i
        elif arr[i] > x:
            fib = fib2
            fib1 = fib1 - fib2
            fib2 = fib - fib1
        else:
            return i
    if fib1 and gap + 1 < len(arr) and arr[gap + 1] == x:
        return gap + 1
    return -1


# arr = [1, 3, 5, 7, 9, 11, 13]
# target = 7
#
# print("Binary:", binary_search(arr, target))       # → 3
# print("Fibonacci:", fibonacci_search(arr, target)) # → 3