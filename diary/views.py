import datetime

from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, \
     DetailView, TemplateView
from django.urls import reverse, reverse_lazy
from .models import Entry
from .forms import NewEntryForm


# Create your views here.

class EntryListView(ListView):
    model = Entry
    template_name = "diary/list_entries.html"
    today = datetime.datetime.now().date()
    extra_context = {"today": today}
    
    def get_queryset(self):
        return Entry.objects.all().order_by("date_for")

def searching(request):
#     if not "searching" in request.COOKIES:
#         search = request.COOKIES.get("searching", "searching")
#     else:
#         search = request.COOKIES["searching"]
    #response = request(render, "diary/entries_list.html", {"searcho": searcho})
    #response.set_cookie("searching", search)
    #return response
    query = request.POST.get("oh")
    if request.method == "POST":
        if query == "":
            searcho = "EMPTO!"
            que = ""
        elif query != "":
            print("GUBBINS", query)
            que = Entry.objects.filter(detail__icontains=query).order_by("date_for")
            searcho = "YAT!"
    today = datetime.datetime.now().date()
    return render(request, "diary/list_entries.html", {"searchu": searcho, "object_listy":que,
                                                        "today": today})
    

class DetailEntryView(DetailView):
    model = Entry
    template_name="diary/detail_entry.html"

class NewEntryView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Entry
    template_name = "diary/new_entry.html"
    fields = (
        "title",
        "detail",
        "user",
        "date_for"
        )
    success_url = "/diary/"
    success_message = "Diary entry saved successfully!"

    def form_valid(self, form):
        form.instance.created = datetime.datetime.now().date()
        form.instance.last_modified = datetime.datetime.now().date()
        print(form.instance.created)
        
        print(form.instance.date_for)
        return super().form_valid(form)

class DeleteEntryView(LoginRequiredMixin, DeleteView):
    model = Entry
    template_name = "diary/delete_entry.html"
    success_url = reverse_lazy("diary:home")
    success_message = "Deleted!"
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(DeleteEntryView, self).delete(request, *args, **kwargs)

class UpdateEntryView(LoginRequiredMixin, UpdateView):
    model = Entry
    fields = ("title",
              "detail",
              "user",
              "date_for")
    template_name = "diary/edit_entry.html"
    
    def form_valid(self, form):
        form.instance.last_modified = datetime.datetime.now().date()
        #print(form.instance.date_for < datetime.datetime.now().y())
        
        return super().form_valid(form)
    
# class HomePageView(TemplateView):
#     template_name = "diary/home2.html"
        
# def hello(request):
#     plinth = "Yaroo"
#     bup = [1,2,3,4,5]
#     response = render(request, "diary/index.html", {"plinth": plinth, "bup": bup})
#     return response

