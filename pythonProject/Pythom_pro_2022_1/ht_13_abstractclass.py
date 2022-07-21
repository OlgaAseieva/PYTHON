
# task 13
"""
1) Создайте ABC класс с абстрактным методом проверки целого числа на
простоту. Т.е., если параметром этого метода является целое число и оно
простое, то метод должен вернуть True, а в противном случае False.
2) Создайте класс его наследующий.
3) Создайте класс, который не наследует пользовательский ABC класс, но
обладает нужным методом. Зарегистрируйте его в качестве виртуального
подкласса.
4) Проверьте работоспособность проекта.
"""


from  abc import ABC, abstractmethod

class A(ABC):

    def __init__(self, num):
        self.check_z_num(num)
        self.num = num

    @classmethod
    def check_z_num(cls, num):
        if not isinstance(num, int):
            raise TypeError('num must be int')

    @abstractmethod
    def check_prime_num(self):
      pass


class Test_num(A):

    def __init__(self, num):
        self.check_z_num(num)
        self.num = num

    def check_prime_num(self):
        for i in range(1, self.num):
            for k in range(2, i):
                if not i % k:
                    break
            else:
                yield i, True
        else:
            yield i, False



x = Test_num(10)
for i in x.check_prime_num():
    print(i)
