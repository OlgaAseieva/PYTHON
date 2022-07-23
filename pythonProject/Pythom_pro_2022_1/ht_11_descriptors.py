# # 11.1
# """
# Создайте дескриптор, который будет делать поля класса управляемые им
# доступными только для чтения.
#
# """
# class AreaDiscrip:
#
#     def __get__(self, instance, owner):
#         p = (instance.x + instance.y + instance.z)/2
#         area = (p *(p-instance.x)*(p-instance.y)*(p-instance.z))**0.5
#         return area
#
#     def __set__(self, instance, value):
#         raise AttributeError
#
# class Triangle:
#
#     def __init__(self, a, b, c):
#         self.x = a
#         self.y = b
#         self.z = c
#
#     area = AreaDiscrip()
#
#     def __str__(self):
#         return f'{self.x} x {self.y} x {self.z}'
#
# x_1 = Triangle(10, 20, 30)
#
# print(x_1.area)
# print(x_1)


#11.2
"""

2) Реализуйте функционал, который будет запрещать установку полей класса
любыми значениями, кроме целых чисел. Т.е., если тому или иному полю
попытаться присвоить, например, строку, то должно быть возбужденно
# исключение.
#
# """
# import datetime
#
#
# class Triangle_1:
#
#     def __init__(self, a, b, c):
#         self.x = a
#         self.y = b
#         self.z = c
#
#     def __setattr__(self, key, value):
#         if isinstance(value, int | float) and value > 0:
#             self.__dict__[key] = value
#         else:
#             raise TypeError("It must be int or float")
#
#     def __str__(self):
#         return f'{self.x} x {self.y} x {self.z}'
#
# x_3 = Triangle_1(1, -2, 3)
#
# print(x_3)




# 11.3
"""

3) Реализуйте свойство класса, которое обладает следующим 
функционалом: при установки значения этого свойства в файл с заранее 
определенным названием должно сохранятся время (когда устанавливали 
значение свойства) и установленное значение.
"""
import datetime

class Triangle_2:

    def __init__(self, a, b, c):
        self.x = a
        self.__y = b
        self.__z = c

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        with open ('test.txt', 'w') as f:
            res_str = f'{datetime.datetime.now()}, {value} \n'
            f.write(res_str)
            self.__x = value

    def __str__(self):
        return f'{self.__x} x {self.__y} x {self.__z}'

x = Triangle_2(1, 5, 7)
print(x)
print(x.x)
