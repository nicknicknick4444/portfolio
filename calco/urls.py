from django.urls import path
from . import views

app_name = "calco"

urlpatterns = [
    path("first/", views.first, name="first"),
    path("colour/", views.colour_pick, name="colour"),
    path("", views.calc1, name="calc1"),
    path("key_process/", views.key_process, name="key_process"),
    path("", views.banty, name="banto")
    ]
