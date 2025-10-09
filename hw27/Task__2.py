def fib_search(arr, target):
    n = len(arr)

    fib_prev2 = 0
    fib_prev1 = 1
    fib_curr  = fib_prev1 + fib_prev2

    while fib_curr < n:
        fib_prev2 = fib_prev1
        fib_prev1 = fib_curr
        fib_curr  = fib_prev1 + fib_prev2

    pos = -1

    while fib_curr > 1:

        i = min(pos + fib_prev2, n - 1)

        if arr[i] < target:
            pos = i
            fib_curr  = fib_prev1
            fib_prev1 = fib_prev2
            fib_prev2 = fib_curr - fib_prev1

        elif arr[i] > target:
            fib_curr  = fib_prev2
            fib_prev1 = fib_prev1 - fib_prev2
            fib_prev2 = fib_curr - fib_prev1
        else:
            return i

    if fib_prev1 and (pos + 1) < n and arr[pos + 1] == target:
        return pos + 1

    return -1

arr = [1, 3, 5, 7, 9, 11, 13, 15]

print(fib_search(arr, 7))   # 4
print(fib_search(arr, 2))   # -1
print(fib_search(arr, 15))  # 7
# Бінарний пошук: час O(log₂ n), пам’ять O(1) (ітеративно).

# Пошук Фібоначчі: час O(log n) (~1.44·log₂ n порівнянь), пам’ять O(1).

# Порівняння: обидва вимагають відсортований масив і мають логарифмічний час.
# На практиці бінарний пошук зазвичай трохи швидший і простіший, тому його беруть за замовчуванням.
# Фібоначчі-пошук — інший варіант, корисний там, де вигідні послідовні зсуви індексів/доступ до пам’яті.