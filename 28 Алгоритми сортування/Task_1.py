def new_sort(items, left_right=False):
    a = items[:]
    n = len(a)
    if n < 2:
        return a

    left, right = 0, n - 1
    swapped = True
    pass_num = 1

    while swapped:
        swapped = False
        if left_right:
            print(f"\nПрохід #{pass_num} вправо: [{left}:{right}]")
        new_right = left
        for i in range(left, right):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                swapped = True
                new_right = i
                if left_right:
                    print(f"  swap {a}")
        right = new_right

        if not swapped:
            break

        swapped = False
        pass_num += 1


        if left_right:
            print(f"\nПрохід #{pass_num} вліво: [{left}:{right}]")
        new_left = right
        for i in range(right, left, -1):
            if a[i - 1] > a[i]:
                a[i - 1], a[i] = a[i], a[i - 1]
                swapped = True
                new_left = i
                if left_right:
                    print(f"  swap {a}")
        left = new_left - 1
        pass_num += 1

    return a


if __name__ == "__main__":
    raw = input("Введіть числа через пробіл: ")
    numbers = [int(x) for x in raw.split()]

    print("\nДо сортування:", numbers)
    sorted_numbers = new_sort(numbers, left_right=True)
    print("\nПісля сортування:", sorted_numbers)

#  Коли доречно:
#
# майже відсортовані масиви (раннє завершення);
#
# коли великі елементи «застрягли» зліва, а малі — справа (потрібно «розібрати» обидва краї);
#
# невеликі обсяги даних, де важлива стабільність.
# Складність: гірш./сер. — O(n²), найкращий (майже відсортовано) — близько O(n).