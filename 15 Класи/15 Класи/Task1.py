
class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
        self.talk() # тут і викликаемо функцію щоб при створенні екземпляра вона виконувалась

    def talk(self):
        print(f"Привіт, мене звати :{self.name}  {self.surname}, і мені {self.age}")

P1 = Person("Mykhailo", "Velychko", 39)
# перевіримо атрибути екземпляра класу
print(P1.__dict__)