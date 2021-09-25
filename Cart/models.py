from django.db import models

from Products.models import Products


# Create your models here.

class UserCart(models.Model):
    slug = models.SlugField()
    user_name = models.CharField(max_length=100)

    def get_full_price(self):
        return sum([i.get_price() for i in self.user.all()])

    def __str__(self):
        return self.user_name


class CartItem(models.Model):
    user = models.ManyToManyField(UserCart, blank=True, related_name="user")
    products = models.ForeignKey(Products, blank=True, on_delete=models.CASCADE, unique=True)
    count = models.PositiveSmallIntegerField()
    username = models.CharField(max_length=300)

    def get_price(self):
        return self.count * self.products.price

    def __str__(self):
        return f"{self.products.title}({self.username})"
