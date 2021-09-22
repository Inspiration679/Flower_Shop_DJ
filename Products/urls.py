from django.urls import path
from Products import views

urlpatterns = [
    path("", views.showProducts.as_view(), name="show_products"),
    path("<int:slug>", views.ShowNeededProduct.as_view(), name="show_necessary_product")
]
