from django.shortcuts import render


# Create your views here.
def ShowHome(request):
    return render(request, "../templates/home.html", {"title": "Home", "path": "css/home/Home.css"})
