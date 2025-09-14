# Task 1
# A bubble sort can be modified to "bubble" in both directions.
# The first pass moves "up" the list and the second pass moves "down."
# This alternating pattern continues until no more passes are necessary.
# Implement this variation and describe under what circumstances it might be appropriate.

def new_bubble_sort(my_list):
    flag = True
    start = 0
    end = len(my_list) - 1

    while flag:
        flag = False

        for i in range(start, end):
            if my_list[i] > my_list[i + 1]:
                my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
                flag = True

        if not flag:
            break

        flag = False
        end -= 1

        for i in range(end - 1, start - 1, -1):
            if my_list[i] > my_list[i + 1]:
                my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
                flag = True

        if not flag:
            break

        start += 1

    return my_list

my_list = [5, 12, 45, 12, 88, 0, 2]
print(my_list)
print(new_bubble_sort(my_list))

print('It might be appropriate when the list is almost sorted, for example, after small updates.')