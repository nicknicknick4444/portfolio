from django.urls import path
from . import views2

app_name = "plp"

urlpatterns = [
    path("submity/",views2.subbo, name="submity"),
    path("", views2.picn, name="index"),
    ]
