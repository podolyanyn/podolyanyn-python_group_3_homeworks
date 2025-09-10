#=============================================================== 1 bidirectional bubble sort =====================================================
"""Task 1

A bubble sort can be modified to "bubble" in both directions. The first pass moves "up" the list and the second pass moves "down." This alternating pattern continues until no more passes are necessary. Implement this variation and describe under what circumstances it might be appropriate."""

def both_directions_bubble_sort(array):
    left_border = 0
    right_border = len(array) - 1
    move = 'right'

    while left_border < right_border:
        if move == 'right':
            for i in range(left_border, right_border):
                if array[i] > array[i + 1]:
                    array[i], array[i + 1] = array[i + 1], array[i]
            right_border -= 1
            move = 'left'
            continue

        if move == 'left':
            for i in range(right_border, left_border, -1):
                if array[i] < array[i - 1]:
                    array[i], array[i - 1] = array[i - 1], array[i]
            left_border += 1
            move = 'right'

# TESTING >>>>>>>>>>>>>>>>>>>>>>
arr = [5, 1, 4, 2, 8, 0, 2]
print(arr)
both_directions_bubble_sort(arr)
print(arr)

#=============================================================== 2 =====================================================
"""Task 2

Implement the mergeSort function without using the slice operator."""

def merge_sort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left_half = [array[i] for i in range(mid)]
        right_half =[array[i] for i in range(mid, len(array))] #array[mid:]
        print(left_half)
        print(right_half)
        merge_sort(left_half)
        merge_sort(right_half)

        i = 0
        j = 0
        k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] <= right_half[j]:
                array[k] = left_half[i]
                i = i + 1
            else:
                array[k] = right_half[j]
                j = j + 1
            k = k + 1

        while i < len(left_half):
            array[k] = left_half[i]
            i = i + 1
            k = k + 1

        while j < len(right_half):
            array[k] = right_half[j]
            j = j + 1
            k = k + 1
        print(f'result left = {left_half}, result right = {right_half}')