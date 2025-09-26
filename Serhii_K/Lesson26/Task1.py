# Task 1:
# Реалізувати алгоритм бінарного пошуку за допомогою рекурсії.

def binary_recursive_search(iterable, value: any, min: int = 0, max: int = 0) -> int:
    """Функція приймає любий ВІДСОРТОВАНИЙ ітерабельний масив елементів
    і виконує бінарний пошук value за допомогою рекурсії"""
    if max == 0:
        max = len(iterable)
    # З кожною ітерацією функція звужує інтервал пошуку
    # Якщо межі інтервалу пошуку становляться некоректними, значить значення не знайдено - повертаємо -1
    if max <= min:
        return -1
    else:
        # Інакше для кожноє наступної ітерації корегуємо min max інтервали пошуку
        mid = (min + max) // 2
        # Якщо поточне значення більше шуканого, то зменьшуємо max і переходимо на наступний рекурсивний цикл
        if iterable[mid] > value:
            return binary_recursive_search(iterable, value, min, mid - 1)
        # Якщо поточне значення меньше шуканого, то збільшуємо min і переходимо на наступний рекурсивний цикл
        elif iterable[mid] < value:
            return binary_recursive_search(iterable, value, mid + 1, max)
        # Інакше шукане значення знайдено - повертаємо його позицію в iterable
        else:
            return mid

# Використання:
if __name__ == '__main__':

    # Пошук в черзі deque:
    from collections import deque
    a = deque([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print(f"Індекс входження 7 = {binary_recursive_search(a, 7)}")

    # Пошук в рядку тексту:
    s = 'abcdefg'
    print(f"Індекс входження 'd' = {binary_recursive_search(s, 'd')}")

    # Пошук в списку:
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"Індекс входження 4 = {binary_recursive_search(l, 4)}")
    print(f"Індекс входження 15 = {binary_recursive_search(l, 15)}")     # -1 (число не знайдено)
