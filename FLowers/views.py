from django.shortcuts import render

def showFlowers(request):
    return render(request,"Flowers.html",{"title":"Flowers","path":"css/MainPage/style.css"})
