class User:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email
        self.validate(email)

    @classmethod
    def validate(cls, email: str):
        if "@" not in email or email.count("@") != 1:
            raise ValueError(" Email має містити один символ '@'")

        user_part, domain_part = email.split("@")

        if not user_part:
            raise ValueError(" Перед '@' має бути ім'я користувача")

        if "." not in domain_part:
            raise ValueError(" Після '@' має бути домен з крапкою (наприклад: gmail.com)")

        if domain_part.startswith(".") or domain_part.endswith("."):
            raise ValueError(" Крапка не може бути на початку або в кінці домену")

        print(f" Email '{email}' успішно пройшов перевірку.")

    def __str__(self):
        return f"Користувач: {self.name}, Email: {self.email}"

while True:
    try:
        name = input("Введіть ім'я користувача: ")
        email = input("Введіть email: ")

        user = User(name, email)
        print(user)
        break  # вихід, якщо email правильний

    except ValueError as e:
        print("Помилка:", e)
        print("Спробуйте ще раз.\n")