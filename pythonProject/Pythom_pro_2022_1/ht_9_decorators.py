# 9.1.1
"""
Создайте декоратор, который будет подсчитывать, сколько раз была
вызвана декорируемая функция.
"""
def decor_count(f):

    def wrapp(*args, **kwargs):
        wrapp.count +=1
        return f(*args, **kwargs)
    wrapp.count = 0
    return wrapp

@decor_count
def any_func(x, y):
    return x +y

print(any_func(1, 4), ", times: ", any_func.count)
print(any_func(2, 4), any_func.count)
print(any_func(3, 6), any_func.count)


# 9.1.2

def decor(f):
    count = 0
    def inner (*args, **kwargs):
        nonlocal count
        count +=1
        return f(*args, **kwargs), count
    return inner

@decor
def greet(name):
    return f'Hello {name}!'

print(greet('Olha'))
print(greet('Oleh'))


# #9.2
# """
# Создайте декоратор, который зарегистрирует декорируемую функцию в
# списке функций, для обработки последовательности.
# """
# def regitrator_f(f):
#     list_func =[]
#     def wrapper(item):
#         if not f in list_func:
#             list_func.append(f)
#         return list_func
#     return wrapper
#
# @regitrator_f
# def rule_1(item):
#     return item**2
#
# @regitrator_f
# def rule_2(item):
#     return not item % 2
#
# @regitrator_f
# def rule_3(item):
#     return item % 2
#
# print(rule_1(3))
# print(rule_2(3))
# print(rule_3(3))
# print(list(list_func))


