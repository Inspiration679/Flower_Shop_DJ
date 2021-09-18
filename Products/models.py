from django.db import models

# Create your models here.
class Products(models.Model):
    product_image = models.ImageField(upload_to="images/product_images/")
    product_title = models.CharField(max_length=300)
