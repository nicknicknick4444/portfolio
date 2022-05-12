import datetime

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
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
                    date_change_help, filter_func, today, cookie_eat
from .email_send import main as email_main

# Create your views here.

def EntryListView2(request):
    object_list_raw = Entry.objects.all().order_by("date_for", "user", "title")
    
    object_list = [i for i in object_list_raw if i.is_old == False]
    user_query = User.objects.values_list("first_name", "last_name")
    USER_CHOICES2 = [i for i in user_query]
    template = "diary/list_entries.html"
    
    paginator = Paginator(object_list, 3)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    response = render(request, template, {"today": today(), "object_list": page_obj,
                                      "users_list": USER_CHOICES2})

    cookie_eat(request.COOKIES, response)
    return response

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
    paginator = Paginator(que3, 3)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    response =  render(request, "diary/list_entries.html", {"searchu": searcho, "object_list": page_obj,
                                                        "today": today(), "users_list": USER_CHOICES2,
                                                       "word_query": query_s, "user_query": query_u,
                                                       "date_query": query_d, "saved": saved,
                                                       "page_obj": page_obj, })
    response.set_cookie("query_s", query_s)
    response.set_cookie("query_u", query_u)
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
    
    paginator = Paginator(cleared_query, 3)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    response = render(request, template, {"searchu": searcho, "object_list": page_obj,
                                        "today": today(), "users_list": USER_CHOICES2,
                                      "saved": saved,})    
    cookoes = ["query_s", "query_u", "query_d"]
    for i in cookoes:
        response.delete_cookie(i)
    
    #pinfo = request.META.get("PATH_INFO")
    #http_host = request.META.get("HTTP_HOST")    
    return response

class DetailEntryView(DetailView):
    model = Entry
    template_name="diary/detail_entry.html"
    
    def render_to_response(self, context, **response_kwargs):
        response = super(DetailView, self).render_to_response(context, **response_kwargs)
        refero = self.request.META.get("HTTP_REFERER")
        urly = cookie_help(self.request.COOKIES, "URLY", refero)
        response.set_cookie("URLY", refero)
        return response

class DeleteEntryView(LoginRequiredMixin, DeleteView):
    model = Entry
    template_name = "diary/delete_entry.html"
    success_url = reverse_lazy("diary:home")
    success_message = "Deleted!"
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(DeleteEntryView, self).delete(request, *args, **kwargs)
    
    def render_to_response(self, context, **response_kwargs):
        response = super(DeleteView, self).render_to_response(context, **response_kwargs)
        refero = self.request.META.get("HTTP_REFERER")
        urly = cookie_help(self.request.COOKIES, "URLY", refero)
        response.set_cookie("URLY", refero)
        return response
    
@login_required
def NewEntryView2(request):
    user_query = User.objects.values_list("first_name", "last_name")
    USER_CHOICES2 = [i for i in user_query]
    new_title = request.POST.get("new_title")
    new_detail = request.POST.get("new_detail")
    new_user = request.POST.get("new_user")
    new_date = request.POST.get("new_date")
    curr_user = request.user.first_name
    
    refero = request.META.get("HTTP_REFERER")
    urly = cookie_help(request.COOKIES, "URLY", refero)
    
    template = "diary/new_entry.html"
    context = {"users_list": USER_CHOICES2}
    response = render(request, template, context)
    if request.method == "POST":
        if convert_date(new_date) >= datetime.datetime.now().date():
            Entry.objects.create(title=new_title, detail=new_detail, \
                                        user=new_user, date_for=convert_date(new_date), \
                                 created=today(), last_modified=today(), \
                                 mod_by=curr_user, by=curr_user)
            messages.success(request, "Entry saved!")
            return HttpResponseRedirect(reverse("diary:home"))
        else:
            context = {"users_list": USER_CHOICES2, "signal": "Date can't be in the past!"}
            
            #response = render(request, template, context)
            response.set_cookie("URLY", refero)
            return response
    else:
        
        #return render(request, template, context)
        response.set_cookie("URLY", refero)
        return response

@login_required
def UpdateEntryView2(request, pk):
    user_query = User.objects.values_list("first_name", "last_name")
    USER_CHOICES2 = [i for i in user_query]
    the_entry = get_object_or_404(Entry, pk=pk)
    title = request.POST.get("edit_title")
    detail = request.POST.get("edit_detail")
    user = request.POST.get("edit_user")
    date = request.POST.get("edit_date")
    
    template = "diary/edit_entry.html"
    context = {"title": title, "detail": detail,
                                      "user": user, "date": date,
                                      "entry": the_entry, 
                                      "users_list": USER_CHOICES2,
                                      "selected_user": the_entry.user}

    refero = request.META.get("HTTP_REFERER")
    urly = cookie_help(request.COOKIES, "URLY", refero)
    
    if request.method == "POST":
        if convert_date(date) >= datetime.datetime.now().date():
            the_entry.title = title
            the_entry.detail = detail
            the_entry.user = user
            the_entry.mod_by = request.user.first_name
            the_entry.date_for = convert_date(date)
            the_entry.last_modified = today()
            the_entry.save()
            
            all_entries = Entry.objects.all().order_by("date_for")
            messages.success(request, "Entry updated!")
            response = HttpResponseRedirect(reverse("diary:back_before"))
            return response
        else:
            context = {"title": title, "detail": detail, "user": user, "date": date,
                       "entry": the_entry, "users_list": USER_CHOICES2,
                       "selected_user": the_entry.user, "signal": "Date can't be in the past!"}
            response = render(request, template, context)
            #response.set_cookie("URLY", refero)
            return response
    else:
        response = render(request, template, context)
        response.set_cookie("URLY", refero)
        return response

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
    template = "diary/list_entries.html"
    messages.success(request, "Emails sent!")
    sent = cookie_help(request.COOKIES, "sent_signal", "SENT!")
    HttpResponseRedirect.allowed_schemes.append("127.0.0.1")
    response = HttpResponseRedirect(request.META.get("HTTP_REFERER"))
    response.set_cookie("sent_signal", sent)
    return response

def hideo(request):
    toggley = cookie_help(request.COOKIES, "vanisho", "GONE!")
    HttpResponseRedirect.allowed_schemes.append("127.0.0.1")
    response =  HttpResponseRedirect(request.META.get("HTTP_REFERER"))
    if "vanisho" in request.COOKIES:
        response.delete_cookie("vanisho")
    elif "vanisho" not in request.COOKIES:
        response.set_cookie("vanisho", toggley)
    return response

def back_to_before(request):
    HttpResponseRedirect.allowed_schemes.append("127.0.0.1")
    redirecty = request.COOKIES["URLY"]
    response = HttpResponseRedirect(redirecty)
    response.delete_cookie("URLY")
    return response

