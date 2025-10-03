class Product:
    def __init__(self, product_type, name, price):
        if price < 0:
            raise ValueError("Ціна не може бути від'ємною")
        self.product_type = product_type
        self.name = name
        self.price = price

    def __repr__(self):
        return f"{self.name} ({self.product_type}) — {self.price:.2f} грн"


class ProductStore:
    def __init__(self):
        self.products = {}
        self.income = 0.0

    def _find_product(self, name_part):

        name_part = name_part.lower()
        for product in self.products:
            if name_part in product.name.lower():
                return product
        return None

    def add(self, product, amount):
        if amount <= 0:
            raise ValueError("Кількість повинна бути більше 0")

        price_with_margin = product.price * 1.3  # +30%
        if product in self.products:
            self.products[product]["quantity"] += amount
        else:
            self.products[product] = {"quantity": amount, "price": price_with_margin}

    def set_discount(self, identifier, percent, identifier_type="name"):
        if percent < 0 or percent > 100:
            raise ValueError("Відсоток знижки має бути від 0 до 100")

        for product in self.products:
            if (identifier_type == "name" and product.name.lower() == identifier.lower()) or \
               (identifier_type == "type" and product.product_type.lower() == identifier.lower()):
                self.products[product]["price"] *= (1 - percent / 100)

    def sell_product(self, product_name, amount):
        product = self._find_product(product_name)
        if not product:
            raise ValueError("Товар не знайдено")
        if self.products[product]["quantity"] < amount:
            raise ValueError("Недостатньо товару для продажу")

        self.products[product]["quantity"] -= amount
        self.income += self.products[product]["price"] * amount

    def get_income(self):
        return round(self.income, 2)

    def get_all_products(self):
        print("\n  Список товарів:")
        for product, info in self.products.items():
            print(f"{product.name} ({product.product_type}) — {info['quantity']} шт., "
                  f"ціна: {info['price']:.2f} грн")

    def get_product_info(self, product_name):
        product = self._find_product(product_name)
        if not product:
            raise ValueError("Товар не знайдено")
        return product.name, self.products[product]["quantity"]

p = Product("Спорт", "Футбольна футболка", 100)
p2 = Product("Їжа", "Рамен", 1.5)

s = ProductStore()
s.add(p, 10)
s.add(p2, 300)

s.sell_product("рамен", 10)  # можна з малої букви
s.set_discount("їжа", 10, identifier_type="type")

s.get_all_products()
print("\nДохід магазину:", s.get_income())
print("Інфо про Рамен:", s.get_product_info("рамен"))