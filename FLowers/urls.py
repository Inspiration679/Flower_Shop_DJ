from django.urls import path
from .views import showFlowers

urlpatterns = [
    path("", showFlowers, name="show_flowers")
]
