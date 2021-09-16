from django.urls import path
from .views import showContacts
urlpatterns=[
    path("",showContacts,name="show_contacts")
]
