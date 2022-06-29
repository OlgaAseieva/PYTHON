import datetime
from buyer import Buyer
from product import Product


class Oder:

    """
    Class for added the cart for buyer and calculate the total amount
    """
    def __init__(self, buyer : Buyer, *arg, **kwargs):
        self.customer = buyer
        self.purchase = []
        self.quantity = []

    def add_cart (self, dish : Product, q : int, *arg, **kwargs):
        if  not  isinstance(dish.price, (int, float)) or not  isinstance(q, int ):
            raise TypeError ('Args must be right types!')
        if dish not in self.purchase:
            self.purchase.append(dish)
            self.quantity.append(q)
        else:
            k = self.purchase.index (dish)
            self.quantity[k] += q
      #  print('oder:', '\n', ''.join(map(str, self.purchase)), ' --', ''.join(map(str, self.quantity)),'\n')

    def info_client (self):
        return f'{self.customer}'

    def total_amount (self):
        total = sum([self.quantity[i] * item.price for i, item in enumerate(self.purchase)])
        return total

    def __str__(self):
        final = f'oder: {datetime.date.today()} \n '
        final += f' {self.customer} \n'

        for i, item in enumerate(self.purchase):
            tmp = f'\t {item} x {self.quantity[i]} = {self.quantity [i] * item.price} \n '
            final += tmp
        final += f' \n Total amount: {self.total_amount()} UAH'
        return final

