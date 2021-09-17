from django.shortcuts import render, get_object_or_404
from .models import Flowers


def showFlowers(request):
    flowers = Flowers.objects

    return render(request, "Flowers.html",
                  {"title": "Shop", "path": "css/Flowers/style.css", "all_path": "css/All.css", "flowers": flowers})
def ShowNecessaryFlower(request, flower_id):
    page=get_object_or_404(Flowers,pk=flower_id)
    return render(request,"Flower_Page.html",{"flower_info":page,"path": "css/Necessary_Flower/style.css", "all_path": "css/All.css",})
