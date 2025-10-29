import asyncio
import time
from multiprocessing import Pool

async def fib_async(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for i in range(2, n+1):
        a, b = b, a + b
    return b

async def fact_async(n):
    res = 1
    for i in range(2, n+1):
        res *= i
    return res

async def square_async(n):
    return n * n

async def cube_async(n):
    return n * n * n

def fib_proc(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a + b
    return b

def fact_proc(n):
    res = 1
    for i in range(2, n+1):
        res *= i
    return res

def square_proc(n):
    return n * n

def cube_proc(n):
    return n * n * n

numbers = list(range(1, 11))

async def main_async():
    start = time.time()
    fib_list = await asyncio.gather(*(fib_async(i) for i in numbers))
    fact_list = await asyncio.gather(*(fact_async(i) for i in numbers))
    square_list = await asyncio.gather(*(square_async(i) for i in numbers))
    cube_list = await asyncio.gather(*(cube_async(i) for i in numbers))
    end = time.time()
    print("Async time:", end - start)
    return fib_list, fact_list, square_list, cube_list

def main_proc():
    start = time.time()
    with Pool() as p:
        fib_list = p.map(fib_proc, numbers)
        fact_list = p.map(fact_proc, numbers)
        square_list = p.map(square_proc, numbers)
        cube_list = p.map(cube_proc, numbers)
    end = time.time()
    print("Proc time:", end - start)
    return fib_list, fact_list, square_list, cube_list


if __name__ == "__main__":
    fib_a, fact_a, square_a, cube_a = asyncio.run(main_async())
    print("Async fib:", fib_a)
    print("Async fact:", fact_a)
    print("Async square:", square_a)
    print("Async cube:", cube_a)

    fib_p, fact_p, square_p, cube_p = main_proc()
    print("Proc fib:", fib_p)
    print("Proc fact:", fact_p)
    print("Proc square:", square_p)
    print("Proc cube:", cube_p)