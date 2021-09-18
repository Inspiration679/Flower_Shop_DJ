from django.shortcuts import render

# Create your views here.
def showAbout(request):
    return render(request, "about.html", {"title": "About", "path": "css/About/about.css", "all_path": "css/head_body.css"})
