from django.db import models

# Create your models here.
class Flowers(models.Model):
    flower_image = models.ImageField(upload_to="images/flower_images/")
    flower_title = models.CharField(max_length=300)
