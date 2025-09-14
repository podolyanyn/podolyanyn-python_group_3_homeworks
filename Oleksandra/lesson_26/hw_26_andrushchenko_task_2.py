def fibonacci_search(arr, x):

    if not arr:
        return -1

    n = len(arr)

    # Ініціалізація чисел Фібоначчі
    fib_m_2 = 0  # (m-2)-е число Фібоначчі
    fib_m_1 = 1  # (m-1)-е число Фібоначчі
    fib_m = fib_m_1 + fib_m_2  # m-е число Фібоначчі

    # Знаходимо найменше число Фібоначчі >= n
    while fib_m < n:
        fib_m_2 = fib_m_1
        fib_m_1 = fib_m
        fib_m = fib_m_2 + fib_m_1

    offset = -1  # зміщення

    while fib_m > 1:
        i = min(offset + fib_m_2, n - 1)

        if arr[i] < x:
            fib_m = fib_m_1
            fib_m_1 = fib_m_2
            fib_m_2 = fib_m - fib_m_1
            offset = i
        elif arr[i] > x:
            fib_m = fib_m_2
            fib_m_1 = fib_m_1 - fib_m_2
            fib_m_2 = fib_m - fib_m_1
        else:
            return i

    # Перевірка останнього елемента
    if fib_m_1 == 1 and offset + 1 < n and arr[offset + 1] == x:
        return offset + 1

    return -1

def binary_search(arr, x):

    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# --- Тестування ---
if __name__ == "__main__":
    sorted_list = [10, 22, 35, 40, 45, 50, 80, 82, 85, 90, 100]
    target = 85

    print(f"Список для пошуку: {sorted_list}")
    print(f"Fibonacci Search: {fibonacci_search(sorted_list, target)}")
    print(f"Binary Search: {binary_search(sorted_list, target)}")


# Fibonacci Search не швидший за Binary Search в загальному випадку, але він може бути
# ефективнішим для великих масивів, які зберігаються на зовнішній пам’яті (через менш
# частий доступ до елементів).