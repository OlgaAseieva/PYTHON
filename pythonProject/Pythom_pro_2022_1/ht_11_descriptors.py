# 11.1
"""
Создайте дескриптор, который будет делать поля класса управляемые им
доступными только для чтения.

"""
class MyDiscrip:
    def __init__(self, val):
        self.val = val

    def __get__(self, instance, owner):
        return "Hi" + self.val

    def __set__(self, instance, value):
        raise AttributeError("READ ONLY")

    def __del__(self):
        raise AttributeError("YOU CAN NOT DEL")

class Stud:

    def __init__(self, name, group):
        self.group = group
        self. name = MyDiscrip

    def __str__(self):
        return f'{self.name} - {self.group}'


st1= Stud('Olha', 'PPro')
st1.name = "as"
print(st1)



# #11.2
# """
#
# 2) Реализуйте функционал, который будет запрещать установку полей класса
# любыми значениями, кроме целых чисел. Т.е., если тому или иному полю
# попытаться присвоить, например, строку, то должно быть возбужденно
# исключение.
#
# """
#
# class Group:
#
#     def __init__(self, name):
#         self.name = name
#
#     # def __getattribute__(self, item):
#     #     try:
#     #         return object.__getattribute__(self, item)
#     #     except AttributeError('new field must be int'):
#     #         if isinstance(item, int):
#     #             print(item)
#     def __getattribute__(self, item):
#         if isinstance(item, int) or item == "name":
#             return object.__getattribute__(self, item)
#         else:
#             raise AttributeError('new field must be int')
#
#     def __getattr__(self, item):
#         if isinstance(item, int):
#             print(item)
#             return __getattr__(self, item)
#         else:
#             raise AttributeError('new field must be int')
#
#     def __str__(self):
#         return f"{self.name}"
#
#
#
# g = Group('ol')
# print(g)
# g.name =5
# g.age = 10
# g.1 = 4
# print(g.__dict__)
#



# 11.3
"""

3) Реализуйте свойство класса, которое обладает следующим 
функционалом: при установки значения этого свойства в файл с заранее 
определенным названием должно сохранятся время (когда устанавливали 
значение свойства) и установленное значение.
"""
