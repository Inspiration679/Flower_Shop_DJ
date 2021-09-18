from django.shortcuts import render


# Create your views here.
def showContacts(request):
    return render(request, "Contacts.html",{"title":"Contacts","path":"css/Main_page/style.css"})
