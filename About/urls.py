from django.urls import path
from .views import showAbout
urlpatterns=[
    path("",showAbout.as_view(),name="show_about")
]
