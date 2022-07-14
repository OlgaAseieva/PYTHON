#8.1 Function as object
"""
Реализуйте генераторную функцию, которая будет возвращать по одному
члену числовой последовательности, закон которой задается с помощью
пользовательской функции. Кроме этого параметром генераторной функции
должны быть значение первого члена прогрессии и количество выдаваемых
членов последовательности (n). Генератор должен остановить свою работу
или по достижению n — го члена , или при передаче команды на завершение.
"""
def seq_generat(n : int, rule):
    return (rule(item) for item in range(n))

def rule_1(item):
    return item **2

def rule_2(item):
    return item **3

def rule_3(item):
    return item % 2

print(*seq_generat(10, rule_1))
print(*seq_generat(10, rule_2))
print(*seq_generat(40, rule_3))
print('*'*10, '\n')

# 8.2
"""
Используя функцию замыкания реализуйте такой прием программирования 
как Мемоизация - https://en.wikipedia.org/wiki/Memoization
Используйте полученный механизм для ускорения функции рекурсивного 
вычисления n — го члена ряда Фибоначчи. Сравните скорость выполнения с 
просто рекурсивным подходом.
"""

import timeit
def timeit_f(method):

    def timed(*args, **kwargs):
        ts = timeit.timeit()
        result = method(*args, **kwargs)
        te = timeit.timeit()
        print (te-ts)
        return result
    return timed

def memoize(func):
    coun_f ={}
    def wrapp (*args):
        if args in coun_f:
            return coun_f[args]
        else:
            coun_f[args] = func(*args)
            return coun_f[args]

        return wrapp

@timeit_f
def fibonach_gen(n:int):
    first_n = 0
    second_n = 1
    index = 1
    while index < n:
        next_n = first_n + second_n
        first_n = second_n
        second_n = next_n
        index +=1
        yield next_n

@memoize
@timeit_f
def fibonach_recurs(n:int):
    if n in (1, 2):
        return 1
    return fibonach_recurs(n-1) + fibonach_recurs(n-2)

for item in fibonach_gen(10):
    print(item)


# 8.3
"""
Напишите функцию, которая применит к списку чисел произвольную 
пользовательскую функцию и вернет суммы элементов полученного списка
"""

def sum_seg(f):
    def user_wrepp(**kwargs):
        return sum(f(**kwargs))
    return user_wrepp
seq= int(map(list, input("enter swq:")))





