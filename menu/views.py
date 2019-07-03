from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Pizza, Burgers, Pasta, Drinks

def index(request):
    pizza = Pizza.objects.order_by('numb').filter(is_pub=True)
    burgers = Burgers.objects.order_by('numb').filter(is_pub=True)
    pasta = Pasta.objects.order_by('numb').filter(is_pub=True)
    drinks = Drinks.objects.order_by('numb').filter(is_pub=True)

    context = {
        'pizza': pizza,
        'burgers': burgers,
        'pasta': pasta,
        'drinks': drinks
    }

    return render(request, 'menu/menu.html', context)
