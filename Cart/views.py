from .models import UserCart, CartItem
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.http import HttpResponse


# Create your views here.
def show_cart(request):
    user_products = get_object_or_404(UserCart, id=request.user.id)

    template = "bucket.html"
    context = {"title": "Cart", "path": "css/cart/cart.css", "cart_products": user_products}

    return render(request, template, context=context)



def add_item(request):
    if request.method == 'GET':
        product_id = request.GET.get('param_first')
        adding = CartItem.objects.get(products__id=product_id, user__user_name__iexact=request.user.username)
        if adding.count < 9:
            adding.count += 1
            adding.save()
        print("hui")

    return HttpResponse(f'''<div id="{adding.products.id}">
<span class="block1__span">{adding.get_price()}</span>
<span class="block1__span">{adding.count}</span>
</div>''')


def remove_item(request):
    if request.method == 'GET':
        product_id = request.GET.get('param_first')
        removing = CartItem.objects.get(products__id=product_id, user__user_name__iexact=request.user.username)
        if removing.count > 1:
            removing.count -= 1
            removing.save()
        print(removing.get_price())

    return HttpResponse(f'''<div id="{removing.products.id}">
    <span class="block1__span">{removing.get_price()}</span>
    <span class="block1__span">{removing.count}</span>
    </div>''')


def remove_cart(request):
    delete_cart = CartItem.objects.get(products__id=request.GET["id"], user__user_name__iexact=request.user.username)
    delete_cart.delete()
    return redirect("show_cart")
