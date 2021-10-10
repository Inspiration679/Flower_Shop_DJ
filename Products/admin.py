from django.contrib import admin
from .models import *

# Регистрация модели товара
admin.site.register(Product)

# Регистрация модели категорий
admin.site.register(ProductTag)

# Регистрация модели товара
admin.site.register(Composition)
admin.site.register(Brand)
admin.site.register(Size)
admin.site.register(Season)
admin.site.register(Specification)
