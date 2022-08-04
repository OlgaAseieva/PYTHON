from django.db import models

class Category(models.Model):

    title = models.CharField(unique=True, max_length=50, db_index=True)
    position = models.SmallIntegerField(unique=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title}'

class Meta:
    ordering = ('position', 'is_visible', 'date')

class Menu(models.Model):

    name = models.CharField(unique=True, max_length=50, db_index=True)
    ingrid = models.CharField(max_length=150)
    descript = models.CharField(max_length=300)
    price = models.FloatField()
    special_dish = models.BooleanField(default=False)
    photo = models.ImageField()

    def __str__(self):
        return f"{self.name}\n{self.ingrid} ________ {self.price} '


class Event(models.Model)

    title = models.CharField(unique=True, max_length=50, db_index=True)
    descript = models.CharField(max_length=300)
    price = models.FloatField()
    date_ev = models.DateField()
    is_visible = models.BooleanField(default=False)
    photo = models.ImageField()

    def __str__(self):
        return f"{self.title}\n{self.date_ev}\n {self.descript}\n {self.price} '

class Galery (models.Model):

