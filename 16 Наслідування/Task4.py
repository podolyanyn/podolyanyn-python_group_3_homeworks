import math
import datetime
class CustomException(Exception):
    def __init__(self, msg):
        super().__init__(msg)
        with open("logs.txt", "a", encoding="utf-8") as file:
            file.write(f"{datetime.datetime.now()} - {msg}\n")


class MathCalculator:
    def log(self, value, base=10):
        if value <= 0:
            raise CustomException(f"Логарифм не визначений для значення {value}")
        if base <= 0 or base == 1:
            raise CustomException(f"Основа логарифма повинна бути > 0 і ≠ 1. Задано: {base}")

        result = math.log(value, base)
        print(f"log_{base}({value}) = {result}")
        return result


calc = MathCalculator()

try:
    calc.log(100)  # Коректний логарифм
    calc.log(-6)  # Помилка: значення ≤ 0
except CustomException as p:
    print(f" Помилка: {p}")

try:
    calc.log(10, 1)  # Помилка: основа = 1
except CustomException as p:
    print(f" Помилка: {p}")

try:
    calc.log(0, 2)  # Помилка: значення = 0
except CustomException as p:
    print(f" Помилка: {p}")

print("\nПрограма працює далі...")