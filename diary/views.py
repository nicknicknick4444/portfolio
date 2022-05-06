import datetime

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, \
     DetailView, TemplateView
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from .models import Entry, SendTime
from .forms import NewEntryForm, CreateUserForm, SetTimeForm, UpdateViewForm
from .service import convert_date, cookie_help, search_change_help, user_change_help, \
                    date_change_help, filter_func, today
from .email_send import main as email_main

# Create your views here.
# def today():
#     return datetime.datetime.now().date()

class EntryListView(ListView):
    model = Entry
    paginate_by = 3
    template_name = "diary/list_entries.html"
    saved = ""
    extra_context = {"today": today(), "saved": saved, }
    
    def get_context_data(self, *args, **kwargs):
        user_query = User.objects.values_list("first_name", "last_name")
        USER_CHOICES2 = [i for i in user_query]
        context = super().get_context_data(*args, **kwargs)
        context["users_list"] = USER_CHOICES2
        return context
    
    def get_queryset(self):
        object_list = Entry.objects.all().order_by("date_for")
        return [i for i in object_list if i.is_old == False]

def EntryListView2(request):
    object_list_raw = Entry.objects.all().order_by("date_for", "user", "title")
    
    object_list = [i for i in object_list_raw if i.is_old == False]
    user_query = User.objects.values_list("first_name", "last_name")
    USER_CHOICES2 = [i for i in user_query]
    template = "diary/list_entries.html"
    
    paginator = Paginator(object_list, 2)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    return render(request, template, {"today": today(), "object_list": page_obj,
                                      "users_list": USER_CHOICES2})

def searching(request):
    user_query = User.objects.values_list("first_name", "last_name")
    USER_CHOICES2 = [i for i in user_query]
    users_list = [i for i in USER_CHOICES2]
    query_s = request.POST.get("term_search")
    query_u = request.POST.get("sort_user")
    if query_u == None:
        query_u = ""

    
    raw_query_d = request.POST.get("by_date")
    
    if "query_d" not in request.COOKIES:
        if raw_query_d != "":
            query_d = convert_date(raw_query_d)
        elif raw_query_d == "":
            query_d = ""
        else:
            query_d = ""
    else:
        query_d = ""
          
    query_s = cookie_help(request.COOKIES, "query_s", query_s)
    query_u = cookie_help(request.COOKIES, "query_u", query_u)
    query_d = cookie_help(request.COOKIES, "query_d", query_d)

    if request.method == "POST" or "query_s" in request.COOKIES:
            
        query_s = search_change_help(request.method, request.COOKIES, "query_s", request.POST.get("term_search"), query_s)
        if "query_u" in request.COOKIES:
            query_u = user_change_help(request.COOKIES, "query_u", request.POST.get("sort_user"), request.method, request.COOKIES["query_u"])
         
        query_d = date_change_help(request.COOKIES, "query_d", request.POST.get("by_date"))        
        que3 = filter_func(query_s, query_u, query_d)
    
    if len(que3) == 0:
        searcho = "EMPTY!"
    else:
        searcho = "SEARCHING!"
    saved = ""
    
    que3 = [i for i in que3]
    
    #Pagination
    paginator = Paginator(que3, 2)
    print(paginator)
    page_number = request.GET.get("page")
    print(page_number)
    page_obj = paginator.get_page(page_number)
        
    print("MOST!!", query_u, type(query_u))
    response =  render(request, "diary/list_entries.html", {"searchu": searcho, "object_list": page_obj,
                                                        "today": today(), "users_list": USER_CHOICES2,
                                                       "word_query": query_s, "user_query": query_u,
                                                       "date_query": query_d, "saved": saved,
                                                       "page_obj": page_obj, })
    response.set_cookie("query_s", query_s)
    response.set_cookie("query_u", query_u)
    print(query_u, type(query_u), "GUSPY!")
    response.set_cookie("query_d", query_d)
    return response

def clear_query(request):
    cleared_query_raw = Entry.objects.all().order_by("date_for", "user", "title")
    cleared_query = [i for i in cleared_query_raw if i.is_old == False]
    saved = ""
    user_query = User.objects.values_list("first_name", "last_name")
    USER_CHOICES2 = [i for i in user_query]
    users_list = [i for i in USER_CHOICES2]
    searcho = "CLEARED!"
    template = "diary/list_entries.html"
    
    paginator = Paginator(cleared_query, 2)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    response = render(request, template, {"searchu": searcho, "object_list": page_obj,
                                        "today": today(), "users_list": USER_CHOICES2,
                                      "saved": saved,})    
    cookoes = ["query_s", "query_u", "query_d"]
    for i in cookoes:
        response.delete_cookie(i)
    
    pinfo = request.META.get("PATH_INFO")
    http_host = request.META.get("HTTP_HOST")
    
    print("BOURCEY!!!!", http_host + pinfo)
    
    return response

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
    
def NewEntryView2(request):
    user_query = User.objects.values_list("first_name", "last_name")
    USER_CHOICES2 = [i for i in user_query]
    new_title = request.POST.get("new_title")
    new_detail = request.POST.get("new_detail")
    new_user = request.POST.get("new_user")
    new_date = request.POST.get("new_date")
    
    if request.method == "POST":
        Entry.objects.create(title=new_title, detail=new_detail, 
                                    user=new_user, date_for=convert_date(new_date),
                             created=today, last_modified=today, mod_by=request.user.first_name,
                             by=request.user.first_name)
        messages.success(request, "Entry saved!")
        return HttpResponseRedirect(reverse("diary:home"))
    else:
        return render(request, "diary/new_entry.html", {"today": today(), "users_list": USER_CHOICES2})

def UpdateEntryView2(request, pk):
    user_query = User.objects.values_list("first_name", "last_name")
    USER_CHOICES2 = [i for i in user_query]
    the_entry = get_object_or_404(Entry, pk=pk)
    title = request.POST.get("edit_title")
    detail = request.POST.get("edit_detail")
    user = request.POST.get("edit_user")
    print("spooks! WOO!", the_entry.user)
    date = request.POST.get("edit_date")
    print("SATE", the_entry.date_for)
    if request.method == "POST":
        the_entry.title = title
        the_entry.detail = detail
        the_entry.user = user
        the_entry.mod_by = request.user.first_name
        the_entry.date_for = convert_date(date)
        the_entry.last_modified = convert_date(date)
        the_entry.save()
        
        all_entries = Entry.objects.all().order_by("date_for")
        messages.success(request, "Entry updated!")
        return HttpResponseRedirect(reverse("diary:home"))
    
    template = "diary/edit_entry.html"
    
    return render(request, template, {"title": title, "detail": detail,
                                      "user": user, "date": date,
                                      "entry": the_entry, 
                                      "users_list": USER_CHOICES2,
                                      "selected_user": the_entry.user})

class UpdateEntryView(LoginRequiredMixin, UpdateView):
    model = Entry
    form_class = UpdateViewForm
    extra_context = {"form":form_class}
    template_name = "diary/edit_entry.html"
        
    def form_valid(self, form):
        form.instance.last_modified = datetime.datetime.now().date()
        form.instance.mod_by = self.request.user.first_name
        return super().form_valid(form)

def add_user(request):
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
    return render(request, template, {"object_list": all_entries, "users_list": users_list, 
                                      "today": today(), "saved": saved, "searchu": searcho})
    
def search_all(request):
    all_entries = Entry.objects.all().order_by("date_for")
    user_query = User.objects.values_list("first_name", "last_name")
    USER_CHOICES2 = [i for i in user_query]
    searcho = "SEARCHING!"
    template = "diary/list_entries.html"
    return render(request, template, {"object_list": all_entries, "users_list": USER_CHOICES2,
                                      "all_query": "ALL!", "today": today(), "searchu": searcho,
                                      "word_query": "", "user_query": None, "date_query": ""})

def send_emails(request):
    email_main()
    template = "diary/done.html"
    return render(request, template, {"today": today()})


def hideo(request):
    template = "diary/list_entries.html"
    pinfo = request.META.get("PATH_INFO")
    http_host = request.META.get("HTTP_HOST")
# #     if not "vanisho" in request.COOKIES:
# #         gubby = request.COOKIES.get("vanisho", "GONE!")
# #     else:
# #         gubby = request.COOKIES["vanisho"]
    toggley = cookie_help(request.COOKIES, "vanisho", "GONE!")
    HttpResponseRedirect.allowed_schemes.append("127.0.0.1")
    print("YAZOOOOOOO!", request.META.get("HTTP_REFERER"))
    response =  HttpResponseRedirect(request.META.get("HTTP_REFERER"))
    if "vanisho" in request.COOKIES:
        response.delete_cookie("vanisho")
    elif "vanisho" not in request.COOKIES:
        response.set_cookie("vanisho", toggley)
    #return request, template, {"today": today()}
    return response
