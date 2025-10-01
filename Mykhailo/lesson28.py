# Завдання 1
#
# Бульбашкове сортування можна модифікувати для «бульбашкового» сортування в обох напрямках.
# Перший прохід переміщує список «вгору», а другий прохід — «вниз». Цей чергуючий шаблон продовжується,
# доки більше проходів не буде потрібно.
# Реалізуйте цей варіант і опишіть, за яких обставин він може бути доцільним.
import random

num_list = [random.randint(0,1000) for i in range(5)]
print(num_list)

end =len(num_list)-1
start = 0

def bulba_front(num_list,start,end):
    f = False

    for item in range(start,end):
        if num_list[item] > num_list[item + 1]:
            num_list[item], num_list[item + 1] = num_list[item + 1], num_list[item]
            f = True
    if f == False: # Якщо стався прохід і не відбулося жодної заміни , то список вже відсортований і подальше продовження недоцільне
        print("Сортування завершено")
        return False
    else:
        return num_list


def bulba_reverse(num_list,start,end):
    c=end-1
    f = False
    for item in range(c,start,-1):
        if num_list[item] < num_list[item - 1]:
            num_list[item], num_list[item - 1] = num_list[item - 1], num_list[item]
            f = True
    if f == False: # Якщо стався прохід і не відбулося жодної заміни , то список вже відсортований і подальше продовження недоцільне
        print("Сортування завершено")
        return False
    else:
        return num_list



for element in range(end,start,-1):
    a = bulba_front(num_list,start,element)
    if a == False:
        break
    else:
        a=bulba_reverse(num_list,start,element)
        start = start + 1
        if a == False:
            break
        else:
            continue

print(num_list)
"""" Щодо доцільності може бути корисним , коли максимум знаходиться десь в початку  списку ,
а мінімум навпаки - максимум і мінімум виганяємо на свої місця за раз."""