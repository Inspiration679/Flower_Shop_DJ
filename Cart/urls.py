from django.urls import path
from .views import show_cart, add_item, remove_item, remove_cart

urlpatterns = [
    path("", show_cart, name="show_cart"),
    path("add_item/", add_item, name="click_cart"),
    path("remove_item/", remove_item, name="remove_item"),
    path("remove_cart/", remove_cart, name="remove_cart"),
]
