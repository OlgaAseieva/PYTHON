import datetime
from buyer import Buyer
from product import Product

class Oder:

    """
    Class for added the cart for buyer and calculate the total amount
    """
    def __init__(self, dish, client, q, *arg, **kwargs):
        self.customer = client
        self.perchase = []
        self.quantity = []
        self.dish = dish

    def add_cart (self, *arg, **kwargs):
        # if self.dish not in self.perchase:
        #     self.purchase.append(Product)
        #     self.quantity.append(q)
        # else:
        #     k = self.purchase.index (Product)
        #     self.quantity[k] += 1
        res_list = f'- {self.perchase[i]}  -- {self.quantity[i]}  = {self.quantity[i] * {Product.price}  '
        return res_list
    def info_client (self, client)
        return f'{self.customer}'

    def total_amount (self):
        return sum([getattr(i, 'price') for i in self.perchase])

    def __str__(self):
        return f'oder: {datetime.date.today()} \n {self.customer} \n {res_list}'

