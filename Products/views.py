from django.shortcuts import get_object_or_404
from .models import Products
from django.views import View
from Main.views import MixinView,MixinNeededView


class showProducts(MixinView, View):
    template = "products.html"
    context = {"title": "Products", "path": "css/products/products.css", "all_path": "css/head_body.css",
               "products": Products.objects}


class ShowNeededProduct(MixinNeededView,View):
    template = "product_page.html"
    context = {"path": "css/products/product_page.css", }
    model = Products


