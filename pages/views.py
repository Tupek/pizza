from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Index

def index(request):
    slider = Index.objects.all()

    context = {
        'slider': slider
    }

    return render(request, 'pages/index.html', context)

def contact(request):
    return render(request, 'pages/contact.html')

def menu(request):
    return render(request, 'pages/menu.html')
