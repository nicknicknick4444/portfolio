import datetime

from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, \
     DetailView, TemplateView
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from .models import Entry, USER_CHOICES
from .forms import NewEntryForm
from .service import convert_date


# Create your views here.

today = datetime.datetime.now().date()

def user_choice_inits():
    return [i for i in USER_CHOICES]
    #inits = [i[1] for i in USER_CHOICES]
    

class EntryListView(ListView):
    model = Entry
    template_name = "diary/list_entries.html"
    #today = datetime.datetime.now().date()
    users_list = user_choice_inits()
    extra_context = {"today": today, "users_list": users_list}
    
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
    users_list = user_choice_inits()
    query_s = request.POST.get("term_search")
    query_u = request.POST.get("sort_user")
    raw_query_d = request.POST.get("by_date")
    if raw_query_d != "":
        query_d = convert_date(raw_query_d)
    else:
        query_d = ""
    #query_d = request.POST.get("by_date")
    print("BIRD POO", query_d)
    print("BIRD PISS", (query_d == Entry.objects.filter(id__exact=6).values()[0]["date_for"]))
    #if query_d != None:
    print("plant!", query_d)
    print("SOFFIT", query_s)
    print("START", query_u)
    
    

    if request.method == "POST":
        if query_s != "":
            que1=Entry.objects.filter(detail__icontains=query_s).order_by("date_for")
            print("LOOK!", que1)
        else:
            que1=Entry.objects.all().order_by("date_for")
            #print("CABBAGE!", type(query_s))
            #print("GANT!")
        
        if query_u != None:
            que2 = que1.filter(user__exact=query_u).order_by("date_for")
            print("Little ones chewed on the fucking bones!", que2)
        else:
            que2 = que1
            print("PArBit", que2)
            
        if query_d != "":
            que3 = que2.filter(date_for__exact=query_d).order_by("user", "title")
        elif query_s != "" or query_u != None:
            
            que3 = que2
        else:
            que3 = Entry.objects.none()
    
        print("BOPEN! OXIDE! XANADU!", que3)
        
    
    if len(que3) == 0:
        searcho = "EMPTY!"
    else:
        searcho = "SEARCHING!"
        
    print("TRASS", que2)
        
    #today = datetime.datetime.now().date()
    return render(request, "diary/list_entries.html", {"searchu": searcho, "object_listy":que3,
                                                        "today": today, "users_list": users_list,
                                                       "word_query": query_s, "user_query": query_u,
                                                       "date_query": query_d})
    

def sort_user(request):
    users_list = user_choice_inits()
    query_u = request.POST.get("sort_user")
    print("START", query_u)
    if request.method == "POST":
#         if query == "":
#             usero = "it_is__EMPTY!"
#             quer = ""
#         elif
        if query_u != "":
            quer_user = Entry.objects.filter(user__exact=query_u).order_by("date_for")
            searcho = "YOF!"
    print("HERE IT IS!!!", quer_user)
    print("And now: ", query_u)
    template = "diary/list_entries.html"
#     if not "query_u" in request.COOKIES:
#         queru = request.COOKIES.get("query_u", query_u)
#     else:
#         queru = request.COOKIES["query_u"]
        #today = date_time.date_time.now().date()
    return render(request, template, {"searchu": searcho, "object_listy": quer_user,
                                                       "today":today, "users_list": users_list,
                                                       "user_query": query_u})
def clear_query(request):
    cleared_query = Entry.objects.all().order_by("date_for")
    print("Preeve!", cleared_query)
    users_list = user_choice_inits()
    searcho = "CLEARED!"
    template = "diary/list_entries.html"
    return render(request, template, {"searchu": searcho, "object_listy": cleared_query,
                                        "today": today, "users_list": users_list})
    #return HttpResponseRedirect(reverse("diary:home"))
        


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
    
    def __str__(self):
        return self.user.first_name

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

