# 10.2.
"""
Создайте декоратор класса с параметром. Параметром должна быть
строка, которая должна дописываться (слева) к результату работы метода
__str__.

"""
class DecorClass:
    def __init__(self, cls):
        self.param = 'Hello'
        self.cls = cls

    def __call__(self, *args, **kwargs):
        self.new_inst = self.cls(*args, **kwargs)
        return  self

    def __str__(self):
        return  f'{self.param} {self.new_inst}'

@DecorClass
class Box:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __call__(self, *args, **kwargs):
        return "you call me!"

    def __str__(self):
        return f'{self.x} x {self.y} x {self.z}'

x = Box(10, 20,30)
print(x)
#print(x())
