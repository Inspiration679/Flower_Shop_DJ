from django.shortcuts import render


# Create your views here.
def ShowMainPage(request):
    return render(request, "../templates/main_page.html", {"title": "Home", "path": "css/Main_page/Main_page.css", "all_path": "css/head_body.css"})
