from django.urls import path
from . import views

app_name = "squaresg"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    #path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    #path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("squares/", views.SquaresView.as_view(), name="squares"),
    path("squaresn/", views.RandomSquaresView, name="squares_rand"),
    path("squaresr/", views.resetty, name="resetto"),
    path("squaresr2/", views.resetty2, name="resetto2"),
    #path("/redirect/", views.redirect_view, name="refreshy"),
    #path("<int:question_id>/vote/", views.vote, name="vote"),
#    path("int:question_id/addey/", views.addeyfunc, name="addy"),
    #path("<int:question_id>/addey/", views.AddyChoice, name="addy"),
    path("saveIt/", views.Scoresy, name="scoresyform"),
    ]
