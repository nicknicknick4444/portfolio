import datetime

from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, \
     DetailView, TemplateView
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from .models import Entry, SendTime
from .forms import NewEntryForm, CreateUserForm, SetTimeForm
from .service import convert_date


# Create your views here.

today = datetime.datetime.now().date()

# def user_choice_inits():
#     #USER_CHOICES
#     return [i for i in USER_CHOICES]
#     #inits = [i[1] for i in USER_CHOICES]
    

class EntryListView(ListView):
    model = Entry
    template_name = "diary/list_entries.html"
    #today = datetime.datetime.now().date()
    #users_list = user_choice_inits()
# #     user_query = User.objects.values_list("first_name", "last_name")
# #     USER_CHOICES = [i for i in user_query]
# #     users_list = [i for i in USER_CHOICES]
# #     print(len(users_list))
    saved = ""
    #time_saved = ""
    extra_context = {"today": today, "saved": saved}
    
    def get_context_data(self, *args, **kwargs):
        user_query = User.objects.values_list("first_name", "last_name")
        USER_CHOICES2 = [i for i in user_query]
        context = super().get_context_data(*args, **kwargs)
        context["users_list"] = [i for i in USER_CHOICES2]
        return context
    
    def get_queryset(self):
        return Entry.objects.all().order_by("date_for")

def searching(request):
    ##users_list = user_choice_inits()
    user_query = User.objects.values_list("first_name", "last_name")
    USER_CHOICES2 = [i for i in user_query]
    users_list = [i for i in USER_CHOICES2]
    query_s = request.POST.get("term_search")
    query_u = request.POST.get("sort_user")
    raw_query_d = request.POST.get("by_date")
    if raw_query_d != "":
        query_d = convert_date(raw_query_d)
    else:
        query_d = ""
    if request.method == "POST":
        if query_s != "":
            que1=Entry.objects.filter(detail__icontains=query_s).order_by("date_for")
        else:
            que1=Entry.objects.all().order_by("date_for")        
        if query_u != None:
            que2 = que1.filter(user__exact=query_u).order_by("date_for")
        else:
            que2 = que1
        if query_d != "":
            que3 = que2.filter(date_for__exact=query_d).order_by("user", "title")
        elif query_s != "" or query_u != None:
            que3 = que2
        else:
            que3 = Entry.objects.none()
            
    if len(que3) == 0:
        searcho = "EMPTY!"
    else:
        searcho = "SEARCHING!"
    saved = ""
    
    return render(request, "diary/list_entries.html", {"searchu": searcho, "object_listy": que3,
                                                        "today": today, "users_list": users_list,
                                                       "word_query": query_s, "user_query": query_u,
                                                       "date_query": query_d, "saved": saved,})
    

# # def sort_user(request):
# #     users_list = user_choice_inits()
# #     query_u = request.POST.get("sort_user")
# #     print("START", query_u)
# #     if request.method == "POST":
# # #         if query == "":
# # #             usero = "it_is__EMPTY!"
# # #             quer = ""
# # #         elif
# #         if query_u != "":
# #             quer_user = Entry.objects.filter(user__exact=query_u).order_by("date_for")
# #             searcho = "YOF!"
# #     print("HERE IT IS!!!", quer_user)
# #     print("And now: ", query_u)
# #     template = "diary/list_entries.html"
# # #     if not "query_u" in request.COOKIES:
# # #         queru = request.COOKIES.get("query_u", query_u)
# # #     else:
# # #         queru = request.COOKIES["query_u"]
# #         #today = date_time.date_time.now().date()
# #     return render(request, template, {"searchu": searcho, "object_listy": quer_user,
# #                                                        "today":today, "users_list": users_list,
# #                                                        "user_query": query_u})

def clear_query(request):
    cleared_query = Entry.objects.all().order_by("date_for")
    print("Preeve!", cleared_query)
    #users_list = user_choice_inits()
    saved = ""
    user_query = User.objects.values_list("first_name", "last_name")
    USER_CHOICES2 = [i for i in user_query]
    users_list = [i for i in USER_CHOICES2]
    searcho = "CLEARED!"
    template = "diary/list_entries.html"
    return render(request, template, {"searchu": searcho, "object_listy": cleared_query,
                                        "today": today, "users_list": users_list,
                                      "saved": saved,})
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
        form.instance.by = self.request.user.first_name
        form.instance.mod_by = self.request.user.first_name
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
    #user_query = User.objects.values_list("first_name", "last_name")
    template_name = "diary/edit_entry.html"
    
    def form_valid(self, form):
        form.instance.last_modified = datetime.datetime.now().date()
        form.instance.mod_by = self.request.user.first_name
        #print(form.instance.date_for < datetime.datetime.now().y())
        
        return super().form_valid(form)

    
#     def get_queryset(self):
#         user_query = User.objects.values_list("first_name", "last_name")
#         USER_CHOICES = [i for i in user_query]
#         return user_query

#def set_time(request):
    

def add_user(request):
    #query = request.POST.get("add_user")
    form = CreateUserForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            print("BAUS!!")
            new_user = User.objects.create_user(form.instance.username,
                                           form.instance.email,
                                           form.instance.password,)
            new_user.first_name = form.instance.first_name
            new_user.last_name = form.instance.last_name
            new_user.save()
            saved = "SAVED!"
            return HttpResponseRedirect(reverse("diary:added_user"))
        else:
            saved = "UNSAVED!"
    else:
        saved = "UNSAVED!"
    template = "diary/add_user.html"
    return render(request, template, {"saved": saved, "form": form})
    #return HttpResponseRedirect(reverse("diary:added_user"))

def set_time(request):
    form = SetTimeForm(request.POST)
   # the_time = get_object_or_404(SendTime, pk=1)
    if request.method == "POST":
        if form.is_valid():
            hour = request.POST.get("hour")
            minute = request.POST.get("minute")
            time = "".join([hour, ":", minute])
            if len(SendTime.objects.all()) > 0:
                #the_time = get_object_or_404(SendTime, pk=1)
                the_time = get_object_or_404(SendTime, pk=2)
                the_time.send_time = time
                the_time.save()
            else:
                SendTime.objects.create(send_time=time)
            print(time)
            time_saved = "Time saved!"
    else:
        time_saved = ""
    if len(SendTime.objects.all()) > 0:
        curr_time = SendTime.objects.get(id=2)
    else:
        curr_time = "NOPE"
            
    template = "diary/set_time.html"
    return render(request, template, {"form": form, "time_saved": time_saved, "curr_time": curr_time})
    
def added_user(request):
    saved = "SAVED!"
    user_query = User.objects.values_list("first_name", "last_name")
    USER_CHOICES2 = [i for i in user_query]
    users_list = [i for i in USER_CHOICES2]
    all_entries = Entry.objects.all().order_by("date_for")
    searcho = "USER_ADDED!"
    template = "diary/list_entries.html"
    return render(request, template, {"object_listy": all_entries, "users_list": users_list, 
                                      "today": today, "saved": saved, "searchu": searcho})
    
# class HomePageView(TemplateView):
#     template_name = "diary/home2.html"
        
# def hello(request):
#     plinth = "Yaroo"
#     bup = [1,2,3,4,5]
#     response = render(request, "diary/index.html", {"plinth": plinth, "bup": bup})
#     return response

