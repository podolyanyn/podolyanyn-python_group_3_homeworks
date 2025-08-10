class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"Мене звати {self.name}, мені {self.age} років."


class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def study(self, subject):
        return f"{self.name} вивчає {subject}."


class Teacher(Person):
    def __init__(self, name, age, subject, salary):
        super().__init__(name, age)
        self.subject = subject
        self.salary = salary

    def teach(self):
        return f"{self.name} викладає {self.subject}."


p = Person("Іван", 20)
s = Student("Марія", 16, 10)
t = Teacher("Оксана", 45, "Математика", 15000)

person_attrs = set(p.__dict__.keys())
student_attrs = set(s.__dict__.keys())
teacher_attrs = set(t.__dict__.keys())

common_attrs = person_attrs & student_attrs & teacher_attrs
student_only = student_attrs - teacher_attrs - person_attrs
teacher_only = teacher_attrs - student_attrs - person_attrs

print(f"Спільні атрибути: {common_attrs}")
print(f"Унікальні для Student: {student_only}")
print(f"Унікальні для Teacher: {teacher_only}")