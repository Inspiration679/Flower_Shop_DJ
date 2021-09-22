from django.urls import path
from Products import views

urlpatterns = [
    path("", views.showProducts.as_view(), name="show_products"),
    path("tags/", views.showProducts.as_view(), name="show_tags"),
    path("<int:slug>", views.ShowNeededProduct.as_view(), name="show_necessary_product"),
    path("tags/<int:slug>", views.ShowNeededTag.as_view(), name="show_necessary_tag"),

]
