num_1_100= []
i = 1
while i <= 100:
    num_1_100.append(i)
    i += 1


find_num = []
j = 0
while j < len(num_1_100):
    a = num_1_100[j]
    if a % 7 == 0 and a % 5 != 0:
        find_num.append(a)
    j += 1


print(find_num)