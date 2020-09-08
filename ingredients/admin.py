from django.contrib import admin

from .models import PizzaIngredient, BurgerIngredient


@admin.register(PizzaIngredient)
class PizzaIngredientAdmin(admin.ModelAdmin):
    pass


@admin.register(BurgerIngredient)
class BurgerIngredientAdmin(admin.ModelAdmin):
    pass
