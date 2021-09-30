from django.db import models
from django.shortcuts import reverse
from django.db.models import ManyToManyField


# Модель категорий
class ProductsTags(models.Model):
    title = models.CharField(max_length=300)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    def get_absolut_url(self):
        return reverse("productstags_detail_url", kwargs={"slug": self.slug})


# Модель товара
class Products(models.Model):
    image = models.ImageField(upload_to="images/product_images/")
    title = models.CharField(max_length=30, unique=True)
    tag = models.ManyToManyField(ProductsTags, related_name="products", blank=True)
    slug = models.SlugField(max_length=30, unique=True)
    price = models.PositiveSmallIntegerField()
    season = models.CharField(max_length=10)
    composition = models.CharField(max_length=10)
    brand = models.CharField(max_length=10)
    size = models.PositiveSmallIntegerField()

    def get_absolute_url(self):
        return reverse('show_necessary_product', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title
