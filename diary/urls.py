from django.urls import path
from . import views

app_name = "diary"

urlpatterns = [
    #path("", views.hello, name="indexu"),
    path("<int:pk>/", views.DetailEntryView.as_view(), name="detail"),
    path("<int:pk>/delete/", views.DeleteEntryView.as_view(), name="delete"),
    path("<int:pk>/edit/", views.UpdateEntryView.as_view(), name="edit"),
    path("new/", views.NewEntryView.as_view(), name="new"),
    path("search/", views.searching, name="searchy"),
    path("sort_user/", views.sort_user, name="sorted_user"),
    path("clear_query/", views.clear_query, name="clear_query"),
    path("", views.EntryListView.as_view(), name="home"),
    #path("plinty/", views.HomePageView.as_view(), name="home2"),
    ]
