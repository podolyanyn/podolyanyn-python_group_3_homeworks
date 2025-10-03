def logger(func):
    def wrapper(*args, **kwargs):
        print(" ВИКЛИК ФУНКЦІЇ")

        print(f" Функція: {func.__name__}")

        # Аргументи позиційні
        if args:
            args_list = ", ".join(str(arg) for arg in args)
            print(f"  Позиційні аргументи: {args_list}")
        else:
            print("   Позиційні аргументи: —")

        # Аргументи іменовані (kwargs)
        if kwargs:
            kwargs_list = ", ".join(f"{k}={v}" for k, v in kwargs.items())
            print(f"   Іменовані аргументи: {kwargs_list}")
        else:
            print("   Іменовані аргументи: —")

        print("  Виконання функції не відбувається\n")
    return wrapper

@logger
def add(x, y):
    return x + y

@logger
def square_all(*args):
    return [arg ** 2 for arg in args]

# Тест виклику
add(4, 5)
square_all(1, 2, 3)