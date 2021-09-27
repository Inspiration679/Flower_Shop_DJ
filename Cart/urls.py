from django.urls import path
from .views import *

urlpatterns = [
    path("", show_cart, name="show_cart"),
    path("add_item/", add_item, name="click_cart"),
    path("remove_item/", remove_item, name="remove_item"),
    path("remove_cart/", remove_cart, name="remove_cart"),
    path("get_full_price/", get_full_price, name="get_full_price"),
]
