from django.views import View
from Main.views import MixinView

# Create your views here.


class showContacts(MixinView, View):
    context = {"title": "Contacts", "path": "css/contacts/contacts.css"}
    template = "contacts.html"
