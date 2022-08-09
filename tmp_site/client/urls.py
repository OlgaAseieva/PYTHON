from django.urls import path
from .views import client, client_general

urlpatterns = [
    path('client/<int:client_num>/', client),
    path('', client_general),
]
