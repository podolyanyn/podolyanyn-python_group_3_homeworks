def arg_rules(type_: type, max_length: int, contains: list):
    def decorator(func):
        def wrapper(arg):
            print("  Перевірка аргументу:", arg)

            # Перевірка типу
            if not isinstance(arg, type_):
                print(f"  Помилка: аргумент має бути типу {type_.__name__}")
                return False

            # Перевірка довжини
            if len(arg) > max_length:
                print(f"  Помилка: довжина аргументу перевищує {max_length} символів")
                return False

            # Перевірка обов'язкових фрагментів
            for item in contains:
                if item not in arg:
                    print(f"  Помилка: рядок не містить обов'язковий елемент: '{item}'")
                    return False

            print("  Усі перевірки пройдено!")
            return func(arg)
        return wrapper
    return decorator


# Декорована функція
@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} п'є пепсі у своєму новенькому BMW!"


#   Користувач вводить ім’я або логін
user_input = input("Введи ім'я або логін: ")

#   Виклик функції з перевірками
result = create_slogan(user_input)

#   Вивід результату
if result:
    print("  Результат:", result)
else:
    print("  Функцію не виконано через помилки.")