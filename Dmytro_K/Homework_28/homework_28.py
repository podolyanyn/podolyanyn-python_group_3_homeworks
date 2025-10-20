# Завдання 1 Сортування методом бульбашок можна модифікувати так, щоб «бульбашки» рухалися в обох напрямках.
# Перший прохід переміщує список «вгору», а другий — «вниз».
# Ця чергування продовжується, поки не буде більше необхідності в проходах.
# Реалізуйте цю модифікацію та опишіть, за яких обставин вона може бути доречною.
def cocktail_sort(arr):
    n = len(arr)
    swapped = True
    start = 0
    end = n - 1

    while swapped:
        swapped = False

        # left to right
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        if not swapped:
            break

        swapped = False
        end -= 1

        # right to left
        for i in range(end - 1, start - 1, -1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        start += 1

# це може бути доречним коли список уже в якійсь мірі сортований.
# Найдоречніше місце цій сортувальній шизі в моїх кошмарних сновидіннях про бульбашку,
# яка ганяє по списках які насправді ноди дерев, які насправді графи.

####################################################  Завдання 2  ######################################################
# Реалізуйте функцію mergeSort без використання оператора slice.

def merge_sort(arr, left, right):
    if left >= right:
        return

    mid = (left + right) // 2
    merge_sort(arr, left, mid)
    merge_sort(arr, mid + 1, right)
    merge(arr, left, mid, right)

def merge(arr, left, mid, right):
    temp = []
    i = left
    j = mid + 1

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1

    while i <= mid:
        temp.append(arr[i])
        i += 1
    while j <= right:
        temp.append(arr[j])
        j += 1

    for k in range(len(temp)):
        arr[left + k] = temp[k]







###################################################### Завдання 3  #####################################################
# Один із способів поліпшити швидке сортування — це використовувати сортування вставкою для списків невеликої довжини
# (назвемо це «межею розділення»). Чому це має сенс?
# Реалізуйте швидке сортування заново і використовуйте його для сортування випадкового списку цілих чисел.
# Проведіть аналіз, використовуючи різні розміри списків для межі розділення.


def insertion_sort(arr, left, right):
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def quick_sort(arr, left, right, threshold=10):
    if right - left + 1 <= threshold:
        insertion_sort(arr, left, right)
        return

    pivot = arr[(left + right) // 2]
    i = left
    j = right

    while i <= j:
        while arr[i] < pivot:
            i += 1
        while arr[j] > pivot:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1

    if left < j:
        quick_sort(arr, left, j, threshold)
    if i < right:
        quick_sort(arr, i, right, threshold)


import random
import time

for threshold in [5, 10, 20, 50]:
    arr = [random.randint(0, 10000) for _ in range(1000)]
    start = time.time()
    quick_sort(arr, 0, len(arr) - 1, threshold)
    end = time.time()
    print(f"Threshold {threshold}: {end - start:.6f} sec")

#Для малих списків підійде.
