import datetime
from buyer import Buyer
from product import Product


class Oder:

    """
    Class for added the cart for buyer and calculate the total amount
    """
    def __init__(self, client, *arg, **kwargs):
        self.customer = client
        self.purchase = []
        self.quantity = []

    def add_cart (self, dish, q, *arg, **kwargs):
        if dish not in self.purchase:
            self.purchase.append(dish)
            self.quantity.append(q)
        else:
            k = self.purchase.index (dish)
            self.quantity[k] += 1
        #print('oder:', '\n', ''.join(map(str, self.purchase)), ' --', ''.join(map(str, self.quantity)),'\n')

        return (self.purchase, self.quantity)

    def info_client (self):
        return f'{self.customer}'

    def total_amount (self):
        return sum([self.quantity[i] * item.price for i, item in enumerate(self.purchase)])

    def __str__(self):
        final = f'oder: {datetime.date.today()} \n '
        final += ''.join(map(str, self.customer)) + '\n'
        final += f' {(str(self.purchase[i]) + str(self.quantity[i]))  for i, v in enumerate(self.purchase)} '
        final += f'Total amount: {self.total_amount()} UAH'
        return final

