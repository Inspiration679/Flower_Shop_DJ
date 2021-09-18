from django.urls import path
from Products import views

urlpatterns = [
    path("", views.showProducts, name="show_products"),
    path("<int:product_id>", views.ShowNecessaryProduct, name="show_necessary_product")
]
