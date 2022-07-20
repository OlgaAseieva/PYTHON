# 9.3
"""
Предположим, в классе определен метод __str__, который возвращает
строку на основании класса. Создайте такой декоратор для этого метода,
чтобы полученная строка сохранялась в текстовый файл, имя которого
совпадает с именем класса, метод которого вы декорировали.

"""


def decor(func):
    def inner(*args, **kwargs):
        names = func.__qualname__.split('.')[:-1]
        file = '.'.join(names) + '.txt'
        res = func(*args, **kwargs)
        with open (file, 'w') as f:
            f.write(res)
        return res
    return inner


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @decor
    def __str__(self):
        return f'{self.name}, {self.age}'


x = Person ('Olha', 30)

