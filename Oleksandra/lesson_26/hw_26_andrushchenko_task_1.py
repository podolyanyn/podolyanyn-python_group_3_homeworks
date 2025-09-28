def binary_search_recursive(arr, target, low, high):
    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search_recursive(arr, target, low, mid - 1)
    else:
        return binary_search_recursive(arr, target, mid + 1, high)

def binary_search(arr, target):
    if not arr:
        return -1
    return binary_search_recursive(arr, target, 0, len(arr) - 1)

# --- Тестування ---
if __name__ == "__main__":
    sorted_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]

    print(binary_search(sorted_list, 13))  # 6
    print(binary_search(sorted_list, 12))  # -1
    print(binary_search([], 5))            # -1
