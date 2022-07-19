# 9.1
"""
Создайте декоратор, который будет подсчитывать, сколько раз была
вызвана декорируемая функция.
"""
def decor_count(f):
    def wrapp(x, y):
        wrapp.count +=1
        return f(x, y)
    wrapp.count = 0
    return wrapp

@decor_count
def any_func(x, y):
    return sum(x, y)

any_func(1, 4)
any_func(5, 4)
any_func(7, 4)
print(any_func.count)

