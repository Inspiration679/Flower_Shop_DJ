from django.views import View
from Main.views import MixinView


# Create your views here.
class showAbout(MixinView, View):
    template = "about.html"
    context = {"title": "About", "path": "css/About/about.css"}
