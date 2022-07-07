import datetime
from buyer import Buyer
from product import Product

class OrderIter:
    def __init__(self, wrapped):
        self.wrapped = wrapped
        #self.q_wrapped = q_wrapped
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.wrapped):
            self.index += 1
            return self.wrapped [self.index -1]
                #, self.q_wrapped[self.index -1]
        raise StopIteration

    def __getitem__(self, item):
        if isinstance(item, slice):
            start = item.start or 0
            stop = item.stop or len(self.wrapped)
            step = item.step or 1

            if start < 0 or stop > len(self.wrapped):
                raise IndexError('Start or stop out of range')
            #res = Oder()
            res = []
            for i in range (start, stop, step):
                res.append(self.wrapped[i])
            return res

        elif isinstance(item, int):
            if item < len(self.wrapped):
                return self.wrapped[item]
            return IndexError

        else:
            raise TypeError

    def __len__(self):
        return len(self.wrapped)

class Oder:

    """
    Class for added the cart for buyer and calculate the total amount
    """
    def __init__(self, buyer : Buyer, *arg, **kwargs):
        self.customer = buyer
        self.purchase = []
        self.quantity = []

    def add_cart (self, dish : Product, q : int, *arg, **kwargs):
        if  not  isinstance(dish.price, (int, float)) or not  isinstance(q, int):
            raise TypeError ('Args must be right types!')
        if dish not in self.purchase:
            self.purchase.append(dish)
            self.quantity.append(q)
        else:
            k = self.purchase.index (dish)
            self.quantity[k] += q
      #  print('oder:', '\n', ''.join(map(str, self.purchase)), ' --', ''.join(map(str, self.quantity)),'\n')

    def __iter__(self):
        return OrderIter (self.purchase)

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



