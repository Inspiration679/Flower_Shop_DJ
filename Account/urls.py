from django.urls import path
from .views import LogOut, SignIn,SignUp


urlpatterns = [
    path("", SignIn, name="show_sign_in"),
    path("sign_up/", SignUp, name="show_sign_up"),
    path("sign_out/", LogOut, name="show_sign_out"),

]
