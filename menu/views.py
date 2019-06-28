from django.shortcuts import render

from .models import Pizza, Burgers, Pasta, Drinks

def index(request):
    pizza = Pizza.objects.all()
    burgers = Burgers.objects.all()
    pasta = Pasta.objects.all()
    drinks = Drinks.objects.all()
    context = {
        'pizza': pizza,
        'burgers': burgers,
        'pasta': pasta,
        'drinks': drinks
    }
    return render(request, 'menu/menus.html', context)

def menu(request, menu_id):
    return render(request, 'menu/menu.html')
