from django.urls import path
from .views import showContacts
urlpatterns=[
    path("",showContacts.as_view(),name="show_contacts")
]
