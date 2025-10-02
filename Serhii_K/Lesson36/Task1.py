# Task 1:
# Створіть окремий асинхронний код для обчислення чисел Фібоначчі, факторіалу, квадратів і кубатури для вхідного числа.
# Заплануйте виконання цього коду за допомогою asyncio.gather для списку цілих чисел від 1 до 10.
# Вам потрібно отримати чотири списки результатів відповідних функцій.
#
# Перепишіть код з використанням простих функцій для отримання тих самих результатів,
# але з використанням бібліотеки багатопроцесорної обробки.
# Засічіть час виконання обох реалізацій, дослідіть результати,
# яка реалізація ефективніша, чому ви отримали саме такий результат.

import asyncio
from concurrent.futures import ProcessPoolExecutor
import time

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def square(x):
    return x * x

def cube(x):
    return x * x * x

# Функція Фібоначчі не працює в асінхронному режимі, бо вона рекурсивна.
# Тому доводиться обгортати цю неасінхронну функцію в іншу асинхронну функцію
# з використанням asyncio.to_thread - ChatGPT.
# Інші функції (факторіал, квадрат і куб) можна переробити в асинхронні,
# але для єдинообразності також залишимо їх не асінхронними
# (це також дозволить використовувати їх для варіанту з мультипроцесорністю).

async def async_wrapper(func, n):
    """Функція, яка запускає синхронну функцію в окремому потоці."""
    return await asyncio.to_thread(func, n)


# 1 Варіант - асинхронний метод:
async def async_main():
    start_time = time.perf_counter()

    # Фібоначчі
    tasks = [async_wrapper(fibonacci, i) for i in range(1,11)]
    results  = await asyncio.gather(*tasks)
    print(f"Фібоначі: {results}")

    # Факторіал
    tasks = [async_wrapper(factorial, i) for i in range(1, 11)]
    results = await asyncio.gather(*tasks)
    print(f"Факторіал: {results}")

    # Квадрат
    tasks = [async_wrapper(square, i) for i in range(1, 11)]
    results = await asyncio.gather(*tasks)
    print(f"Квадрат: {results}")

    # Куб
    tasks = [async_wrapper(cube, i) for i in range(1, 11)]
    results = await asyncio.gather(*tasks)
    print(f"Куб: {results}")

    duration = time.perf_counter() - start_time
    print(f"Загальний час (асінхронний метод): {duration:.6f} секунд")  # Загальний час (асінхронний метод): 0.019561 секунд


# 2 Варіант - мультипроцессінг:
def multiprocess_main():
    NUMBERS = [i for i in range(1, 11)]

    start_time = time.perf_counter()

    # Фібоначчі
    with ProcessPoolExecutor() as executor:
        results = list(executor.map(fibonacci, NUMBERS))
    print(f"Фібоначі: {results}")

    # Факторіал
    with ProcessPoolExecutor() as executor:
        results = list(executor.map(factorial, NUMBERS))
    print(f"Факторіал: {results}")

    # Квадрат
    with ProcessPoolExecutor() as executor:
        results = list(executor.map(square, NUMBERS))
    print(f"Квадрат: {results}")

    # Куб
    with ProcessPoolExecutor() as executor:
        results = list(executor.map(cube, NUMBERS))
    print(f"Куб: {results}")

    duration = time.perf_counter() - start_time
    print(f"Загальний час (мультипроцессінг): {duration:.6f} секунд")   # Загальний час (мультипроцессінг): 2.473575 секунд



if __name__ == '__main__':
    asyncio.run(async_main())   # 1 Варіант - асінхронний
    print()
    multiprocess_main()         # 2 Варіант - мультипроцессорний

# Використання асінхронного методу обчислень дало меньший загальний час виконання (0.01 сек.)
# в порівнянні з використанням мультипроцессінгу (2.47 сек).
# Можлива причина чому асинхронний метод виявився швидшим в тому, що задачі дуже прості й легкі для процесора.
# Накладні витрати мультипроцесингу (створення процесів, міжпроцесна комунікація) з'їли всі переваги мультипроцесорності.
# Можливо якби обчислення були більш складними - то перевага була б на стороні мультипроцесорності.