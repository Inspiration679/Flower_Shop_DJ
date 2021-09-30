from .models import Products, ProductsTags
from django.views import View
from Main.views import MixinView, MixinNeededView
from django.shortcuts import redirect, render
from Cart.models import CartItem, UserCart
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET
from django.http import HttpResponse


# Отображение всего товара
class ShowProducts(MixinView, View):
    template = "all_products.html"
    context = {"title": "Products", "path": "css/products/products.css", "all_path": "css/head_body.css",
               "products": Products.objects}


# Отображение выбраного товара
class ShowNeededProduct(MixinNeededView, View):
    template = "product_page.html"
    context = {"path": "css/products/product_page.css", }
    model = Products


# Отображение категории
class ShowNeededTag(MixinNeededView, View):
    template = "tag_products.html"
    context = {"path": "css/products/products.css", }
    model = ProductsTags


# Добавление товара в корзину

@require_GET
def add_to_card(request):
    product_id = request.GET.get('param_first')

    try:
        add_product = CartItem.objects.get(user__user_name__iexact=request.user.username,
                                           products_id__exact=product_id)
    except ObjectDoesNotExist:

        add_product = CartItem.objects.create(products=Products.objects.get(id=product_id), count=1,
                                              username=request.user.username)
        add_product.user.add(UserCart.objects.get(user_name__iexact=request.user.username))
        add_product.save()

    return HttpResponse(f""" <p>{add_product.products.price}₴</p>

                        <button class="" disabled>
                            Добавлено
                        </button>""")


# Приминение фильтров
@require_GET
def show_filtred_products(request):
    kwargs = {i: request.GET[i] for i in request.GET if request.GET[i] != "all"}
    template = "filter.html"

    context = {"path": "css/products/products.css", "products": Products.objects.filter(**kwargs),
               "tag__title": request.GET["tag__title"]}
    return render(request, template, context)
