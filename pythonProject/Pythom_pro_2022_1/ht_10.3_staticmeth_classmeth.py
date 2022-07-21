# 10.3
"""
Для класса Box напишите статический метод, который будет подсчитывать
суммарный объем двух ящиков, которые будут его параметрами.

"""

class Box:
    count =0

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        Box.count += 1

    @classmethod
    def box_number(cls):
        return cls.count


    def __str__(self):
        return f"{self.x} x {self.y} x {self.z}"

    def valume (self):
        return self.x * self.y * self.z

    @staticmethod
    def sum_valume(a, b):
        if isinstance(a, Box) and isinstance(b, Box):
            return a.valume() + b.valume()
        return  None

x = Box(1, 2, 3)
y = Box (10, 20, 30)

print(Box.sum_valume(x, y))
print(Box.box_number())
