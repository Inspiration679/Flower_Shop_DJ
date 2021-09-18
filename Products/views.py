from django.shortcuts import render, get_object_or_404
from .models import Products


def showProducts(request):
    products = Products.objects

    return render(request, "products.html",
                  {"title": "Main", "path": "css/products/products.css", "all_path": "css/head_body.css",
                   "products": products})


def ShowNecessaryProduct(request, product_id):
    page = get_object_or_404(Products, pk=product_id)
    return render(request, "product_page.html",{"product_info": page, "path": "css/products/product_page.css", "all_path": "css/head_body.css", })
