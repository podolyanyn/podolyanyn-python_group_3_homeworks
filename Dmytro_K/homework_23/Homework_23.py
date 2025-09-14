from typing import List, Tuple

# We assume that all lists passed to functions are the same length N

# Match big O complexities with the code snippets below

# answers
# 1 - log n
# 2 - n^2
# 3 - n
# 4 - n^2
# 5 - 1
# 6 - n


def question1(first_list: List[int], second_list: List[int]) -> List[int]:
    res: List[int] = []
    for el_first_list in first_list:
        if el_first_list in second_list:
            res.append(el_first_list)
    return res

# def question1 = folded linear searching in list O(n^2)


def question2(n: int) -> int:
    for _ in range(10):
        n **= 3
    return n

# def question2 = О(1)
# the cycle runs 10 times, and in each iteration, n is raised to the power of 3.
# for i in range(10) is constanta, and n**= 3 is just n * n * n, so the
# complexity is O(n^3), but since it is constant, we can say that the complexity is O(1).


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

# def question3 = n^2
# Begining from copy list showing O(N), because for copying a list of length N takes O(N) time.
# Then we have loop "for el_second_list in second_list", and this loop run M times for
# each element in second_list, so it is O(M).
# Inside this loop, we have another loop "for check in temp", which runs for each element in temp.
# But size of temp is not constant: from begining temp = N, and in the end it can be N + M.
# As BigO notation must looking for the worst case, I think we can say that
# the complexity of this function is M * O(N + M) = O(N * M + M^2) = O(N * M).
# If I simplify this, I can say that the complexity is O(N^2), cause N and M are the same list length.


def question4(input_list: List[int]) -> int:
    res: int = 0
    for el in input_list:
        if el > res:
            res = el
    return res

# def question4 = О(n)
# The function iterates through each element in the input_list exactly once.


def question5(n: int) -> List[Tuple[int, int]]:
    res: List[Tuple[int, int]] = []
    for i in range(n):
        for j in range(n):
            res.append((i, j))
    return res

# def question5 = n^2
# The function generates a list of tuples (i, j) for each pair of indices i and j in the range of n.
# The outer loop runs n times, and for each iteration of the outer loop, the inner loop also runs n times.
# Therefore, the total number of iterations is n * n = n^2.


def question6(n: int) -> int:
    while n > 1:
        n /= 2
    return n

# def question6 = log n
# Every iteration of the loop divides n by 2, so the number of iterations is logarithmic
# in relation to the initial value of n. Specifically, it runs log2(n) times.
