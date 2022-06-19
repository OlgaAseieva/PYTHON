class Product:
    def __init__(self, prod, size, price):
        self.prod = prod
        self.size = size
        self.price = price

    def __str__(self):
        return f'{self.prod}, {self.price} uah, ({self.size} gr)'
