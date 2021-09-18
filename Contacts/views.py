from django.shortcuts import render


# Create your views here.
def showContacts(request):
    return render(request, "contacts.html",{"title":"Contacts","path":"css/contacts/contacts.css","all_path": "css/head_body.css"})
