# Task 1:
# Прості числа
# На вхід подано список чисел, деякі з яких є простими.
# Вам потрібно написати утиліту, яка отримує на вхід число і повертає bool,
# залежно від того, чи є воно простим чи ні.
# Використовуйте ThreadPoolExecutor та ProcessPoolExecutor
# для створення різних паралельних реалізацій для фільтрації NUMBERS.
# Порівняйте результати та продуктивність кожної з них.

# Довідка: Просте число — це натуральне число, більше за 1,
# яке має лише два дільники: одиницю (1) та саме себе (N).
# Порядок перевірки:
# Якщо число менше 2 - воно не є простим.
# Якщо число 2 чи 3 - просте.
# Якщо число парне (крім 2) - складене, 2 - це єдине парне просте число
# Далі перевіряти діленням тільки до квадратного кореня з числа.
# Наприклад, для 29 достатньо перевірити поділ на 2, 3, 5 (бо √29 = 5,3).
# Якщо не ділиться ні на одне - просте.

from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import math
import time



def check_prime(number: int) -> bool:
    """Функція, що перевіряє чи є надане число натуральним"""
    if number < 2:
        return False
    if number in (2, 3):
        return True
    if number % 2 == 0:
        return False
    i = 3
    while i * i <= number:
        if number % i == 0:
            return False
        i += 2
    return True


if __name__ == '__main__':
    NUMBERS = [
        2,  # prime
        1099726899285419,
        1570341764013157,  # prime
        1637027521802551,  # prime
        1880450821379411,  # prime
        1893530391196711,  # prime
        2447109360961063,  # prime
        3,  # prime
        2772290760589219,  # prime
        3033700317376073,  # prime
        4350190374376723,
        4350190491008389,  # prime
        4350190491008390,
        4350222956688319,
        2447120421950803,
        5,  # prime
    ]

    # Список для збереження булевих результатів:
    check_results = []

    # 1. Використання одного головного потоку (для порівняння):
    start_time = time.perf_counter()

    # В циклі обробляємо кожне число одне за одним і отримуємо список булевих результатів перевірки:
    for i in NUMBERS:
        check_results.append(check_prime(i))

    # Друк результатів:
    for i in range(len(NUMBERS)):
        print(NUMBERS[i], check_results[i])

    duration = time.perf_counter() - start_time
    print(f"Перевірено за {duration} сек.")         # Перевірено за 42.444578299997374 сек.


    # # 2. Використання ThreadPoolExecutor
    start_time = time.perf_counter()

    with ThreadPoolExecutor() as executor:
        check_results = list(executor.map(check_prime, NUMBERS))

    # Друк результатів:
    for i in range(len(NUMBERS)):
        print(NUMBERS[i], check_results[i])

    duration = time.perf_counter() - start_time
    print(f"Перевірено за {duration} сек. (Threads)")   # Перевірено за 42.53268439997919 сек. (Threads)


    # Використання ProcessPoolExecutor
    start_time = time.perf_counter()

    with ProcessPoolExecutor() as executor:
        check_results = list(executor.map(check_prime, NUMBERS))

    # Друк результатів:
    for i in range(len(NUMBERS)):
        print(NUMBERS[i], check_results[i])

    duration = time.perf_counter() - start_time
    print(f"Перевірено за {duration} сек. (Processes)") # Перевірено за 25.496505400020396 сек. (Processes)

    # Це - приклад CPU-bound задач, і тому використання ProcessPoolExecutor дало найбільшу продуктивність (25 сек),
    # в порівнянні з використанням ThreadPoolExecutor (42.5 сек) і без використання паралельних обчислень (42.4 сек).