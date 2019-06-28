from django.db import models


class Pizza(models.Model):
    numb = models.IntegerField(unique=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=4, decimal_places=2)
    photo = models.ImageField(upload_to='photos/pizza/')
    is_pub = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Burgers(models.Model):
    numb = models.IntegerField(unique=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=4, decimal_places=2)
    photo = models.ImageField(upload_to='photos/burgers/')
    is_pub = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Pasta(models.Model):
    numb = models.IntegerField(unique=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=4, decimal_places=2)
    photo = models.ImageField(upload_to='photos/pasta/')
    is_pub = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Drinks(models.Model):
    numb = models.IntegerField(unique=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=4, decimal_places=2)
    photo = models.ImageField(upload_to='photos/drinks/')
    is_pub = models.BooleanField(default=True)

    def __str__(self):
        return self.title


# class Cart(models.Model):
#     client = models.ForeignKey(User)
#     food = models.ManyToManyField(Food)
#     address = models.TextField()
