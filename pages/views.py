from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'pages/index.html')

def contact(request):
    return render(request, 'pages/contact.html')

def menu(request):
    return render(request, 'pages/menu.html')

def panel(request):
    return render(request, 'pages/panel.html')
