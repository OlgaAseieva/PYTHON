
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
    def __init__(self, x : int, y : int):
        if not isinstance(x, int) or not isinstance(y, int) or y:
            return None
        else:
            self.x = x
            self.y = y


    def nod(self):
        if y:
            return f' y must be !=0'
        else:
            return math.gcd(self.x, self.y)

    def __add__(self, other):
        if self.y or other.y:
            return f' y must be !=0'
        else:
            a = self.x * other.y + other.x * self.y
            b = self.y * other.y
            #return f' {self.x * other.y + other.x * self.y}/{self.y * other.y}
            return f'{a}/{b}'
    def __str__(self):
        return f'{self.nod()}'

frac1= Proper_fraction(1, 2)
frac2 = Proper_fraction(2, 4)

print(frac1 + frac2)
    # def __mul__(self, other):
    #     if self.b or self.d or self.c:
    #         return ValueError
    #     else:
    #         return f' {self.a * self.c}/{self.b * self.d}
    #
    # def __truediv__(self, other):
    #     if self.b or self.d or self.c:
    #         return ValueError
    #     else:
    #         return f' {self.a * self.d}/{self.b * self.c}

    def __str__(self):
        return f'{self.nod()}'

frac1= Proper_fraction(1, 2)
frac2 = Proper_fraction(2, 4)

print(frac1 + frac2)

