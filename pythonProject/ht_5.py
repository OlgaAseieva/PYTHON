
# # HT_5_1
# class Rectangle:
#     """
#     Создайте класс «Прямоугольник», у которого присутствуют два поля
# (ширина и высота). Реализуйте метод сравнения прямоугольников по
# площади. Также реализуйте методы сложения прямоугольников (площадь
# суммарного прямоугольника должна быть равна сумме площадей
# прямоугольников, которые вы складываете). Реализуйте методы
# умножения прямоугольника на число n (это должно увеличить площадь
# базового прямоугольника в n раз)
#     """
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
#     def sq(self):
#         if isinstance(self.x, int | float) and isinstance(self.y, int | float):
#             return  self.x * self.y
#         else:
#             NotImplemented
#
#     def __gt__(self, other):
#         return  self.sq() > other.sq()
#
#     def __ge__(self, other):
#         return  self.sq() >= other.sq()
#
#     def __lt__(self, other):
#         return  self.sq() < other.sq()
#
#     def __le__(self, other):
#         return  self.sq() <= other.sq()
#
#     def __eq__(self, other):
#         return  self.sq() == other.sq()
#
#     def __add__(self, other):
#         return  self.sq() + other.sq()
#
#     def __mul__(self, n):
#         return  self.sq() * n
#
#     def __str__(self):
#         return f'{x}, {y}'
#
# rect1 = Rectangle(10, 2)
# rect2 = Rectangle(4, 4)
#
# print(rect1*2)
import math

class Proper_fraction:
    '''
     Создайте класс «Правильная дробь» и реализуйте методы сравнения,
сложения, вычитания и произведения для экземпляров этого класса.
    '''

    def __init__(self, x : int, y : int):
        if not isinstance(x, int) or not isinstance(y, int) or not y:
            raise ValueError
        else:
            self.x = x
            self.y = y

    def nod(self, *args, **kwargs):
        if not self.y:
            raise ValueError('div by 0 is not allowed')
        else:
            return math.gcd(self.x, self.y)

    def __add__(self, other):
        if not self.y or not other.y:
            raise ValueError('div by 0 is not allowed')
        else:
            a = self.x * other.y + other.x * self.y
            b = self.y * other.y

            return Proper_fraction(a, b)

    def __sub__(self, other):
        if not self.y or not other.y:
            raise ValueError('div by 0 is not allowed')
        else:
            a = self.x * other.y - other.x * self.y
            b = self.y * other.y

            return Proper_fraction(a, b)

    def __mul__(self, other):
        if not self.y or not other.y:
            raise ValueError('div by 0 is not allowed')
        else:

            a = self.x * other.x
            b = self.y * other.y

            return Proper_fraction(a, b)

    def __truediv__(self, other):
        if not self.y or not other.y:
            raise ValueError('div by 0 is not allowed')
        else:
            a = self.x * other.y
            b = self.y * other.x

            return Proper_fraction(a, b)

    def __gt__(self, other):
         if not self.y or not other.y:
            raise ValueError('div by 0 is not allowed')
         else:
            a = self.x * other.y
            b = self.y * other.x

            return a > b

    def __lt__(self, other):
         if not self.y or not other.y:
            raise ValueError('div by 0 is not allowed')
         else:
            a = self.x * other.y
            b = self.y * other.x

            return a < b

    def __str__(self):
        if self.nod:
            if self.x > self.y:
                k = self.x // self.y
                return f'{k} {int((self.x-k*self.y) /self.nod())}/{int(self.y /self.nod())}'
            else:
                return f'{int(self.x /self.nod())}/{int(self.y /self.nod())}'
        else:
            return f' {self.x}/{self.y}'


frac1 = Proper_fraction(1, 2)
frac2 = Proper_fraction(4, 3)

print(frac1 + frac2)
print(frac1 - frac2)
print(frac1 * frac2)
print(frac1 / frac2)
print(frac2 > frac1)
print(frac1 < frac2)




