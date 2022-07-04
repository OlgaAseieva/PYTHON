import set_ticket
import datetime

class Price_ticket:
    BASE_price = 100
    DATE_EVENT = datetime.datetime(day=1, month= 10, year=2022)
    def __init__ (self):
        self.price = {}

    def price_dict(self):
        self.price[reg] = self.BASE_price
        self.price[adv] = self.BASE_price * 0.6
        self.price[late] = self.BASE_price * 1.1
        self.price[stud] = self.BASE_price * 0.5

        return self.price

    def __str__(self):
        return  print({self.price})

class Client:
    def __init__(self, name, status,  phone, d_event, q):
        self.name = name
        self.status = status
        self.phone = phone
        self.date = datetime.datetime.now()
        self.q = q

    def __str__(self):
        return f'{self.name}, {self.status}, {self.phone}, {self.date}, {self.q}'

class Ticket_sold(Exception):
    def __init__(self, limit, mess):
        super().__init__(Exception)
        self.limit = limit
        self.mess = mess

    def __str__(self):
        return f'{self.limit},{self.mess}'

class Ticket_count:
    DATE_EVENT = ''
    LIMIT = 200
    START_NUMBER = 234543

    def __init__ (self,f, client : Client, kind :Price_ticket):
        self.numb_ticket =[]
        self.price = []
        #self.q = q


    def generate_number(self, START_NUMBER):
        if len(self.numb_ticket) > self.LIMIT:
            raise Ticket_sold (self.LIMIT, f'All tickets are sold')
        else:
            ticket_num = self.START_NUMBER + 1
        return ticket_num

    def def_price (self, client: Client, price : Price_ticket):
         if len(self.numb_ticket) > self.LIMIT:
            raise Ticket_sold (self.LIMIT, f'All tickets are sold')
        elif client.status == 'student':
            pr_tick = Price_ticket.price_dict[stud]
        elif datetime.datetime(day=1, month= 10, year=2022) - client.date  >= 60:
            pr_tick = Price_ticket.price_dict[adv]
        elif datetime.datetime(day=1, month= 10, year=2022) - client.date  <= 10:
            pr_tick = Price_ticket.price_dict[late]
        else:
            pr_tick = Price_ticket.price_dict[reg]
        return pr_tick


    def add_cart (self, client : Client, *arg, **kwargs):
        if  not  isinstance(client, Client):
            raise TypeError ('Args  client enter with error!')

        sum_oder = 0
        tick_oder_index=[]

        for i in range (1,client.q+1)
            if self.generate_number():
                self.numb_ticket.append (self.generate_number())
                self.price.append (self.def_price())
                #tick_oder_index.append((self.generate_number(), self.def_price()))
                sum_oder += self.def_price()
                tick_oder_index.append(len(self.numb_ticket))
        return {tick_oder_index}, {sum_oder}

    def __str__(self):
        res = f'{client.name} {client.phone} \n date of order: {client.date}\n'
        res += f'{self.add_cart()}\n'

        return res


