def analyze_function(func):
    code = func.__code__
    arg_count = code.co_argcount
    local_count = code.co_nlocals
    var_names = code.co_varnames

    print(f"  Аналіз функції: {func.__name__}")
    print(f"  Кількість аргументів: {arg_count}")
    print(f"  Кількість локальних змінних: {local_count}")
    print(f"  Імена змінних: {', '.join(var_names)}")


def example(a, b):
    x = a + b
    y = x * 2
    message = "Привіт"


analyze_function(example)
