from django.urls import path
from .views import showAbout
urlpatterns=[
    path("",showAbout,name="show_about")
]
