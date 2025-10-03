def b_search_recursive(arr, target, left=0, right=None):

    if right is None:
        right = len(arr) - 1

    if left > right:
        return -1

    mid = left + (right - left) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return b_search_recursive(arr, target, left, mid - 1)
    else:
        return b_search_recursive(arr, target, mid + 1, right)

arr = [1, 3, 5, 7, 9, 11]

print(b_search_recursive(arr, 7))   
print(b_search_recursive(arr, 8))