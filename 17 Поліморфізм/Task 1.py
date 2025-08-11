class Animals:
    def talk (self):
        print("Голос тварини")


class Dog(Animals):
    def talk(self):
        super().talk()
        print("Gav")


class Cat(Animals):
    def talk(self):
        super().talk()
        print("Nyav")
def make_talk(wer):
    wer.talk()

dog = Dog()
cat = Cat()

make_talk(dog) 
make_talk(cat)

