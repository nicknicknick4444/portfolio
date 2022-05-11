from django.urls import path
from . import views

app_name = "diary"

urlpatterns = [
    path("<int:pk>/", views.DetailEntryView.as_view(), name="detail"),
    path("<int:pk>/delete/", views.DeleteEntryView.as_view(), name="delete"),
    path("<int:pk>/edit2/", views.UpdateEntryView2, name="edit2"),
    path("new/", views.NewEntryView2, name="new"),
    path("search/", views.searching, name="searchy"),
    path("clear_query/", views.clear_query, name="clear_query"),
    path("all/", views.search_all, name="search_all"),
    path("email/", views.send_emails, name="emails"),
    path("hideo/", views.hideo, name="hideo"),
    path("backo/", views.back_to_before, name="back_before"),
    path("", views.EntryListView2, name="home"),
    ]
