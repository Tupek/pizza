from django.db import models


class PizzaIngredient(models.Model):
    name = models.CharField(max_length=255)


class BurgerIngredient(models.Model):
    name = models.CharField(max_length=255)
