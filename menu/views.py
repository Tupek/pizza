from django.shortcuts import render

def index(request):
    return render(request, 'menu/menus.html')

def menu(request, menu_id):
    return render(request, 'menu/menu.html')
