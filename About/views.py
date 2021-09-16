from django.shortcuts import render

# Create your views here.
def showAbout(request):
    return render(request,"About.html",{"title":"About","path":"css/MainPage/style.css"})
