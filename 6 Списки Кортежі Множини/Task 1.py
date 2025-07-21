List_a=[]
i=0
import random
while i < 10:
    a = random.randint(1,1000)
    List_a.append(a)
    i+=1
print("List of number:",  List_a )


max_a = List_a[0]
max_i = 0
while max_i < len(List_a):
    if List_a[max_i] > max_a:
        max_a = List_a[max_i]
    max_i += 1

print("Max number", max_a)