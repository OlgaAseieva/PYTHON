# 10/1
""""
Создайте декоратор, который зарегистрирует декорируемый класс в
списке классов.
"""

list_class = []

def add_class (cls):
    list_class.append(cls)
    return cls

@add_class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f'{self.name}, {self.age}'

@add_class
class Box:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return  f'{self.x} x {self.y} x {self.z}'

x = list_class[0]('Ol',40)
y = list_class[1](2, 3, 4)

print(x)
print(y)
