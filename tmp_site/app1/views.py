from django.shortcuts import render, HttpResponse, redirect
from .models import Category, Menu, Event, AboutUs, WhytUs, Galery
from .forms import UserReservationForm

# Create your views here.

def base (request):

    if request.method == 'POST':
        reserve = UserReservationForm(request.POST)
        if reserve.is_valid():
            reserve.save()
            return redirect('/')

    # for request.GET:

    categories = Category.objects.filter(is_visible=True)
    menu = Menu.objects.filter(is_visible=True)
    special = Menu.objects.filter(special_dish=True)
    event = Event.objects.filter(is_visible=True)
    whyus = WhytUs.objects.all()
    about = AboutUs.objects.filter(is_visible=True)
    gallery = Galery.objects.filter(is_visible = True)
    reserve = UserReservationForm()

    data = {'categories': categories,
            'menu': menu,
            'special': special,
            'event': event,
            'about': about,
            'whyus': whyus,
            'gallery': gallery,
            'reserve_form': reserve
            }
    return render(request, 'base.html', context=data)
