from .models import Products, ProductsTags
from django.views import View
from Main.views import MixinView, MixinNeededView
from django.shortcuts import redirect, render
from Cart.models import CartItem, UserCart
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required


class ShowProducts(MixinView, View):
    template = "all_products.html"
    context = {"title": "Products", "path": "css/products/products.css", "all_path": "css/head_body.css",
               "products": Products.objects}


class ShowNeededProduct(MixinNeededView, View):
    template = "product_page.html"
    context = {"path": "css/products/product_page.css", }
    model = Products


class ShowNeededTag(MixinNeededView, View):
    template = "tag_products.html"
    context = {"path": "css/products/products.css", }
    model = ProductsTags


@login_required(login_url="/sign/")
def add_to_card(request):
    try:
        CartItem.objects.get(user__user_name__iexact=request.user.username,
                             products_id__exact=request.GET["id"])
    except ObjectDoesNotExist:

        add_product = CartItem.objects.create(products=Products.objects.get(id=request.GET["id"]), count=1,
                                              username=request.user.username)
        add_product.user.add(UserCart.objects.get(user_name__iexact=request.user.username))
        add_product.save()

    return redirect(request.GET["path"])


def show_filtred_products(request):
    kwargs = {i: request.GET[i] for i in request.GET if request.GET[i] != "all"}
    template = "filter.html"

    context = {"path": "css/products/products.css", "products": Products.objects.filter(**kwargs),
               "tag__title": request.GET["tag__title"]}
    return render(request, template, context)
