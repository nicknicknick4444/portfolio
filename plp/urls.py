from django.urls import path
from . import views

app_name = "plp"

urlpatterns = [
    path("submity/",views.subbo, name="submity"),
    path("", views.poy, name="index"),
    ]
