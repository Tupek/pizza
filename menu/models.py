from django.db import models

from ingredients.models import PizzaIngredient, BurgerIngredient


class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=4, decimal_places=2)
    is_published = models.BooleanField(default=False)
    menu_slot = models.IntegerField(unique=True)


class Pizza(MenuItem):
    ingredients = models.ManyToManyField(PizzaIngredient)


class Burger(MenuItem):
    ingredients = models.ManyToManyField(BurgerIngredient)
