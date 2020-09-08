from django.contrib import admin

from .models import Pizza, Burger


@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):
    pass


@admin.register(Burger)
class BurgerAdmin(admin.ModelAdmin):
    pass
