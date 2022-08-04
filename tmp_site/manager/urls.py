from django.urls import path
from .views import manager, menu, event, reserve

urlpatterns = [
    path('', manager),
    path('menu/', menu),
    path('event/', event),
    path('reserv/', reserve),

]
