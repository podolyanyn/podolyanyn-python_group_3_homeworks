def oops():
    user_input = input("Введіть список чисел через пробіл: ")
    try:
        lst = [int(x) for x in user_input.strip().split()]
    except ValueError:
        print("Некоректне введення! Введіть лише числа.")
        return

    try:
        index = int(input("Введіть індекс: "))
    except ValueError:
        print("Індекс має бути цілим числом.")
        return

    if not (-len(lst) <= index < len(lst)):
        raise IndexError("Індекс виходить за межі списку!")

    print(f"Значення за індексом {index}: {lst[index]}")


def catcher():
   try:
       oops()
   except IndexError as e:
       print(f"Перехоплено IndexError: {e}")

catcher()

# Якщо замінити на KeyError то відбудеться аварійне завершення програми блок оброби помилки не виконаеться
# def catcher():
#     try:
#         oops()
#     except KeyError as e:
#         print(f"Перехоплено IndexError: {e}")
#
# catcher()