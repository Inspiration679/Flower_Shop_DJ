from django.shortcuts import render

# Create your views here.
def ShowMainPage(request):
    return render(request,"../templates/MainPage.html")
