from django.shortcuts import render


# Create your views here.
def ShowMainPage(request):
    return render(request, "../templates/MainPage.html", {"title": "Home", "path": "css/MainPage/style.css","all_path":"css/All.css"})
