from django.urls import path
# from .views import signUpView
from .views import signView

urlpatterns=[
    path("",signView,name="show_sign_up_in"),

]
