from django.db import models
from django.shortcuts import reverse
from django.db.models import ManyToManyField


# Create your models here.

class ProductsTags(models.Model):
    title = models.CharField(max_length=300)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    def get_absolut_url(self):
        return reverse("tag_detail_url", kwargs={"slug": self.slug})


class Products(models.Model):
    image = models.ImageField(upload_to="images/product_images/")
    title = models.CharField(max_length=300)
    tag = models.ManyToManyField(ProductsTags, related_name="products")
    slug = models.SlugField(max_length=30, unique=True)

    def get_absolut_url(self):
        return reverse("products_detail_url", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title
