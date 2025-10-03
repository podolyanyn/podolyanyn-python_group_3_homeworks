class Dog:
    age_factor = 7

    def __init__(self):
        self.dog_age = self.get_valid_age()

    def get_valid_age(self):

        while True:
            try:
                age = int(input("Введіть вік собаки у роках: "))
                if age <= 0:
                    print(" Вік має бути більший за 0. Спробуйте ще раз.")
                else:
                    return age
            except ValueError:
                print("  Введіть ціле число, а не букви чи символи.")

    def human_age(self):

        return self.dog_age * Dog.age_factor

my_dog = Dog()
print(f" Вік собаки у людських роках: {my_dog.human_age()}")