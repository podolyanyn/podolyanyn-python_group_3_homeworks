from typing import List, Tuple


# We assume that all lists passed to functions are the same length N

# answers
# 1 - log n
# 2 - n^2
# 3 - n
# 4 - n^2
# 5 - 1
# 6 - n


def question1(first_list: List[int], second_list: List[int]) -> List[int]:
    # Ця функція має вкладений цикл. Зовнішній цикл ітерує N елементів.
    # Оператор `in` для списку в Python має складність O(N) у найгіршому випадку.
    # Отже, загальна складність буде N * N, або O(n^2).
    res: List[int] = []
    for el_first_list in first_list:
        if el_first_list in second_list:
            res.append(el_first_list)
    return res
# Відповідь: 4 - n^2

def question2(n: int) -> int:
    # Ця функція виконує цикл фіксовану кількість разів (10).
    # Час виконання не залежить від значення `n`.
    # Отже, це константна складність O(1).
    for _ in range(10):
        n **= 3
    return n
# Відповідь: 5 - 1

def question3(first_list: List[int], second_list: List[int]) -> List[int]:
    # Ця функція має вкладений цикл.
    # Зовнішній цикл ітерує по `second_list` (N елементів).
    # Внутрішній цикл ітерує по `temp` (який може зростати до 2N).
    # Загальна складність буде приблизно N * N, або O(n^2).
    temp: List[int] = first_list[:]
    for el_second_list in second_list:
        flag = False
        for check in temp:
            if el_second_list == check:
                flag = True
                break
        if not flag:
            temp.append(el_second_list)
    return temp
# Відповідь: 2 - n^2

def question4(input_list: List[int]) -> int:
    # Ця функція ітерує по списку один раз.
    # Час виконання прямо пропорційний довжині списку.
    # Отже, складність O(n).
    res: int = 0
    for el in input_list:
        if el > res:
            res = el
    return res
# Відповідь: 6 - n

def question5(n: int) -> List[Tuple[int, int]]:
    # Ця функція має вкладений цикл, де обидва цикли ітерують до `n`.
    # Кількість операцій буде n * n, що призводить до O(n^2).
    res: List[Tuple[int, int]] = []
    for i in range(n):
        for j in range(n):
            res.append((i, j))
    return res
# Відповідь: 4 - n^2 (Примітка: в оригінальному завданні є дві відповіді n^2)

def question6(n: int) -> int:
    # Цей цикл ділить `n` на 2 на кожній ітерації.
    # Це є типовою поведінкою для логарифмічної складності.
    # Кількість ітерацій буде логарифмом від `n` по основі 2.
    # Отже, складність O(log n).
    while n > 1:
        n /= 2
    return n
# Відповідь: 1 - log n