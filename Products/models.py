from django.db import models
from django.shortcuts import reverse

# Create your models here.
class Products(models.Model):
    image = models.ImageField(upload_to="images/product_images/")
    title = models.CharField(max_length=300)
    slug = models.SlugField(max_length=30,unique=True)

    def get_absolut_url(self):
        return reverse("products_detail_url",kwargs={"slug":self.slug})

    def __str__(self):
        return self.title
