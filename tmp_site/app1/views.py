from django.shortcuts import render, HttpResponse
from .models import Category, Menu, Event, Spesial, AboutUs, WhytUs, Galery

# Create your views here.

def base (request):
    categories = Category.objects.filter(is_visible=True)
    menu = Menu.objects.filter(is_visible=True)
    special = Menu.objects.filter(spesial=True)
    event = Event.objects.filter(is_visible=True)
    whyus = WhytUs.objects.filter(is_visible=True)
    about = AboutUs.objects.filter(is_visible=True)

    data = {'categories': categories,
            'menu': menu,
            'special': special,
            'event' : event,
            'about' : about,
            'whyus' :whyus,
            }
    return HttpResponse('Hi from base page')
