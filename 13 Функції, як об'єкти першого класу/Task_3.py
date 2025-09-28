def choose_func(nums, func_positive, func_with_negatives):
    if all(n > 0 for n in nums):
        print(" Усі числа додатні. Виконуємо func_positive()...")
        return func_positive(nums)
    elif any(n < 0 for n in nums):
        print("  Є від’ємні числа. Виконуємо func_with_negatives()...")
        return func_with_negatives(nums)
    else:
        print("  містить лише нулі або порожній. Повертаємо порожній список.")
        return []

def square_nums(nums):
    return [x ** 2 for x in nums]

def remove_negatives(nums):
    return [x for x in nums if x > 0]

# Тестові дані
nums1 = [1, 2, 3]
nums2 = [0, -1, 2]
nums3 = [0, 0, 0]
nums4 = []

# Виклики
print("  nums1:", choose_func(nums1, square_nums, remove_negatives))
print("  nums2:", choose_func(nums2, square_nums, remove_negatives))
print("  nums3:", choose_func(nums3, square_nums, remove_negatives))
print("  nums4:", choose_func(nums4, square_nums, remove_negatives))