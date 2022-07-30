from django.urls import path
from . import views
import django

app_name = "squaresg"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("squares/", views.SquaresView2, name="squares"),
    path("squaresn/", views.RandomSquaresView, name="squares_rand"),
    path("squaresr/", views.resetty, name="resetto"),
    path("squaresr2/", views.resetty2, name="resetto2"),
    path("squaresr3/", views.resetty3, name="resetto3"),
    path("saveIt/", views.Scoresy, name="scoresyform"),
    path("projects/", views.ProjectsView, name="projects"),
    ]
