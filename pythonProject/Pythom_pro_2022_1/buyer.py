class Buyer:
    def __init__(self, name, surname, phone):
        self.name = name
        self.surname = surname
        self.phone = phone



    def __str__(self):
        return f'{self.name} {self.surname} - {self.phone}'
