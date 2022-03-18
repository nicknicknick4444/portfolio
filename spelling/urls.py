from django.urls import path
from . import views

app_name = "spelling"

urlpatterns = [
    #path("", views.ShowTweets.as_view(), name="index"),
    path("", views.searchy, name="index"),
    path("to_send/", views.sure, name="to_send"),
    path("sending_tweet/", views.sendy, name="sending"),
    path("wordypick/", views.wordPick, name="wordpicking"),
    path("filtdown/", views.filterdown, name="filtdown"),
    path("filtup/", views.filterup, name="filtup"),
    path("voted/", views.closey, name="voted_already"),
    ]
