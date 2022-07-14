# 7.4 Hапишите выражение-генератор для заполнения списка. Список должен
# быть заполнен кубами чисел от 2 и до указанной вами величины.

def list_exp(n):
    start =2
    lisr_exp = []
    exp = 3
    lisr_exp = (i**exp for i in range(start, n))
    return lisr_exp
print(list(list_exp(6)))

# 7.1

def geometr_progression(n):
    """
    Pеализуйте генераторную функцию, которая будет возвращать по
одному члену геометрической прогрессии с указанным множителем.
Генератор должен остановить свою работу или по достижению указанной
границы, или при передаче команды на завершение.
    :return:
    """
    factor = 2
    next_n = 1
    print(next_n)
    index = 0
    while index <= n:
        index += 1
        try:
            next_n = next_n * factor
            st = yield next_n
        except Exception:
            print('Stop')
        if not st:
                factor = st
    return

q = geometr_progression(12)
for item in q:
    print(item)
    if item  > 500:
        print(q.send(5))
    if item  > 1000:
        q.close()
        print (item)



# 7.2

def analog_range(num, *args, **kwargs):
    """
    Реализуйте свой аналог генераторной функции range(). Да, вы теперь
знаете, что это - генератор
    :return:
    """
    print(type(num))
    if isinstance(num, int):
        i=0
        while i < num:
            yield i
            i +=1
        return
    if isinstance(num, slice):
        start = num.start or 0
        stop = num.stop
        step = num.step or 1
        i = start
        if start < 0 or i+step > stop:
            raise  IndexError('index is not in limit')
        while i < stop:
            yield i
            i += step
    if isinstance(num, tuple):
        start, stop, step = num
        start = start or 0
        stop = stop
        step = step or 1
        i = start
        if start < 0 or i+step > stop:
            raise  IndexError('index is not in limit')
        while i < stop:
            yield i
            i += step

for item in analog_range(10):
    print(item)
print("*"*10)
for item in analog_range((2, 10, 2)):
    print(item)

# 7.3.
"""
 Напишите функцию-генератор, которая будет возвращать простые числа. 
Верхняя граница этого диапазона должна быть задана параметром этой 
функции
"""
def prime_number(n):
    if not isinstance(n, int):
        raise TypeError
    for i in range (1, n):
        if i <3:
            yield i
        for j in range (2, i):
            if not i % j:
                break
        else:
            yield  i
            break
    return

print(*prime_number(30))


