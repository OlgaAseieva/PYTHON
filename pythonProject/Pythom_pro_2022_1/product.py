class Negatnum(Exception):
    def __init__(self, value: int| float = None, mess: str = None):
        super().__init__()
        self.value = value
        self.mess = mess
    def __str__(self):
        return f'{self.value} {self.mess}'


class Product:
    def __init__(self, prod : str, size: int, price: int):

        if not isinstance(price, (int,float)):
            raise TypeError()
        if price <= 0:
            raise Negatnum (price, f'price must be positive')
        self.prod = prod
        self.size = size
        self.price = price


    def __str__(self):
        return f'{self.prod}, ({self.size} gr) - {self.price} uah'

#x = Product("rty", 300, -20)
