# Відповідність складностей (Big-O)

# 1 question1 → O(n²) — для кожного елемента першого списку виконується лінійний пошук у другому.

# 1 question2 → O(1) — рівно 10 ітерацій (константа).

# 1 question3 → O(n²) — вкладений лінійний пошук у temp.

# 1 question4 → O(n) — один прохід для пошуку максимуму.

# 1 question5 → O(n²) — подвійний цикл формує n² пар.

# 1 question6 → O(log n) — кожен крок ділить n навпіл.
# виправлення додамо імпорт

from typing import List, Tuple
def question1(first_list: List[int], second_list: List[int]) -> List[int]:
    res: List[int] = []
    for el_first_list in first_list:
        if el_first_list in second_list:
            res.append(el_first_list)
    return res

def question2(n: int) -> int:
    for _ in range(10):
        n **= 3
    return n

def question3(first_list: List[int], second_list: List[int]) -> List[int]:
    temp: List[int] = first_list[:]
    for el_second_list in second_list:
        flag = False
        for check in temp:
            if el_second_list == check:
                flag = True
                break
        if not flag:
            temp.append(second_list)
    return temp

def question4(input_list: List[int]) -> int:
    res: int = 0
    for el in input_list:
        if el > res:
            res = el
    return res

def question5(n: int) -> List[Tuple[int, int]]:
    res: List[Tuple[int, int]] = []
    for i in range(n):
        for j in range(n):
            res.append((i, j))
    return res

def question6(n: int) -> int:
    while n > 1:
        n /= 2
    return n