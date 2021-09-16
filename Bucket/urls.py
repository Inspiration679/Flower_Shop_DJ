from django.urls import path
from .views import showBucket
urlpatterns=[
    path("",showBucket,name="show_bucket")
]
