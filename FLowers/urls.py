from django.urls import path
from FLowers import views

urlpatterns = [
    path("", views.showFlowers, name="show_flowers"),
    path("<int:flower_id>",views.ShowNecessaryFlower,name="show_necessary_flower")
]
