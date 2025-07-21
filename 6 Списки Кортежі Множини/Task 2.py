import random
List_1 = []
i = 0
while i < 10:
    List_1.append(random.randint(1, 10))
    i += 1


List_2=[]
i = 0
while i < 10:
    List_2.append(random.randint(1, 10))
    i += 1

print("First List:", List_1)
print("Second List:", List_2)

set_1 = set(List_1)
set_2 = set(List_2)
# User operation intersection()

Union_List =  set( set_1 & set_2 )

print(list(Union_List))
