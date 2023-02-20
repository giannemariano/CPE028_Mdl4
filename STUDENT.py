class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name}({self.age})"

p1 = Student("Gianne Mariano", 20)
p2 = Student("Mary Kambing", 18)

print(p1)
print(p1.name)
print(p1.age)
print(p2.name)
print(p2.age)