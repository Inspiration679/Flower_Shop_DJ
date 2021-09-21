from django.shortcuts import render

# Create your views here.
def showBucket(request):
    return render(request,"bucket.html",{"title":"Bucket","path":"css/Home/style.css"})
