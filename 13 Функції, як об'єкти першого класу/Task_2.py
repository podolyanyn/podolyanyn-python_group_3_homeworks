def create_vat_calculator(vat_percent):
    def calculate(price):
        return price + (price * vat_percent / 100)
    return calculate

vat20 = create_vat_calculator(20)

# Тепер рахуємо з ПДВ різні ціни
print("Ціна з ПДВ:", vat20(100))  # → 120.0
print("Ціна з ПДВ:", vat20(250))  # → 300.0

# Створимо інший калькулятор, наприклад 7%
vat7 = create_vat_calculator(7)
print("Ціна з ПДВ 7%:", vat7(100))  # → 107.0