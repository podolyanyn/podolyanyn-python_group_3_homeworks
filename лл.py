import random
import functools

# 🔹 Оригінальна функція: повертає кортеж із 10 випадкових чисел
def func():
    """Повертає кортеж з 10 випадкових цілих чисел від 0 до 100."""
    return tuple(random.randint(0, 100) for _ in range(10))

# 🔹 Декоратор: замінює всі не-кратні 2 на None, використовуючи map + lambda
def map_decorator(func):
    """Залишає числа, кратні 2, всі інші замінює на None."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        transformed = tuple(map(lambda x: x if x % 2 == 0 else None, result))
        return transformed
    return wrapper

# 🔹 Застосовуємо декоратор
@map_decorator
def filtered_func():
    """Випадкові числа, фільтровані за кратністю 2."""
    return func()

# 🔸 Тест
original = func()
filtered = filtered_func()

print("Оригінальні числа:")
print(original)

print("\nПісля декоратора (залишено лише ті, що % 2 == 0):")
print(filtered)