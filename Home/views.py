from django.shortcuts import render
from django.views import View
from Main.views import MixinView


# Create your views here.

class ShowHome(MixinView, View):
    template = "home.html"
    context = {"title": "Home", "path": "css/home/Home.css"}
