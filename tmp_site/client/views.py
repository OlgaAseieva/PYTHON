from django.shortcuts import render, HttpResponse

# Create your views here.
def client (request, client_num):
    return HttpResponse(f" Hi from Client page. It's client {client_num}")

def client_general (request):
    return HttpResponse(f" Hi from Client page. It's new client")
