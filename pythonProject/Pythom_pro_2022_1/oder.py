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
        print('oder:', '\n', ''.join(map(str, self.purchase)), ' --', ''.join(map(str, self.quantity)),'\n')
        res_list = ''
        for i in range len (self.quantity):
            res_list += ''.join(map(str, self.purchase[i]))+ ' --'+ ''.join(map(str, self.quantity[i])) + '\n'

        return res_list

    def info_client (self):

        return f'{self.customer}'

    def total_amount (self):
        total = sum([getattr(i, 'price') * self.quantity[i] for i in self.purchase])
        print(total)
        return total

    def __str__(self):
        final = f'oder: {datetime.date.today()} \n '
        final += ''.join(map(str, self.customer)) + '\n'
        final += res_list+'\n'
        final += f'Total amount: {str(total)} UAH'
        return final

