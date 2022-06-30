from django.urls import path
from . import views

app_name = "calco"

urlpatterns = [
    path("first/", views.first, name="first"),
    path("colour/", views.colour_pick, name="colour"),
    path("", views.calc1, name="calc1"),
    path("one/", views.one, name="one"),
    path("", views.banty, name="banto")
    ]
