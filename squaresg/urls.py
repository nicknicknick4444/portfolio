from django.urls import path
from . import views
import django

app_name = "squaresg"

def custom_page_not_found(request):
    return django.views.defaults.page_not_found(request, None)

def custom_server_error(request):
    return django.views.defaults.server_error(request)

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    #path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    #path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    ## ORIG path("squares/", views.SquaresView.as_view(), name="squares"),
    path("squares/", views.SquaresView2, name="squares"),
    path("squaresn/", views.RandomSquaresView, name="squares_rand"),
    path("squaresr/", views.resetty, name="resetto"),
    path("squaresr2/", views.resetty2, name="resetto2"),
    #path("<int:question_id>/vote/", views.vote, name="vote"),
#    path("int:question_id/addey/", views.addeyfunc, name="addy"),
    #path("<int:question_id>/addey/", views.AddyChoice, name="addy"),
    path("saveIt/", views.Scoresy, name="scoresyform"),
#     path("404/", custom_page_not_found),
#     path("500/", custom_server_error),
    ]

#handler404 = "squaresg.views.handler404"
#handler500 = "squaresg.views.handler500"
# handler403 = "squaresg.views.error_403"
# handler400 = "squaresg.views.error_400"
