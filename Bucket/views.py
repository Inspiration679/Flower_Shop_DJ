from django.views import View
from Home.views import MixinView


# Create your views here.
class showBucket(MixinView, View):
    template = "bucket.html"
    context = {"title": "Bucket", "path": "css/Home/style.css"}
