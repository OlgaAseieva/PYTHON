# 9.4.
"""
Создайте декоратор с параметрами для проведения хронометража работы
той или иной функции. Параметрами должны выступать то, сколько раз нужно
запустить декорируемую функцию и в какой файл сохранить результаты
хронометража. Цель - провести хронометраж декорируемой функции

"""
import time

def decorator(file_name, numb):
    def wrapper (func):
        def inner (*args, ** kwargs):
            with open (file_name, 'a') as f:
                for i in range (numb):
                    start = time.time()
                    res = func(*args, **kwargs)
                    stop = time.time()
                    f.write(f'{start} : {stop} : {stop - start} \n')
            return res
        return inner
    return wrapper

@decorator("test.txt", 5)
def fibonachy (n):
    a, b = 0, 1
    for i in range (0, n):
        a, b = b, a + b
    return a

print(fibonachy(50))
