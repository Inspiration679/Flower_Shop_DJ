from django.urls import path
from .views import showBucket
urlpatterns=[
    path("",showBucket.as_view(),name="show_bucket")
]
