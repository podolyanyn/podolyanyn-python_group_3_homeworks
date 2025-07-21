def oops():
    my_list = [1, 2, 3]
    print(my_list[10])  # Тут виникає IndexError

print("Початок")

try:
    oops()  # Тут помилка
except IndexError:
    print("❗ IndexError було перехоплено")

print("Кінець програми")

