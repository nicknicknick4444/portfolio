import datetime

from django.shortcuts import render, get_object_or_404
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
from .service import convert_date, cookie_help, change_help, user_change_help


# Create your views here.

today = datetime.datetime.now().date()

# def user_choice_inits():
#     #USER_CHOICES
#     return [i for i in USER_CHOICES]
#     #inits = [i[1] for i in USER_CHOICES]
    

class EntryListView(ListView):
    model = Entry
    #context_object_list = "object_list"
    paginate_by = 3
    template_name = "diary/list_entries.html"
        
    #today = datetime.datetime.now().date()
    #users_list = user_choice_inits()
# #     user_query = User.objects.values_list("first_name", "last_name")
# #     USER_CHOICES = [i for i in user_query]
# #     users_list = [i for i in USER_CHOICES]
# #     print(len(users_list))
    saved = ""
    #time_saved = ""
    extra_context = {"today": today, "saved": saved, }
    
    def get_context_data(self, *args, **kwargs):
        user_query = User.objects.values_list("first_name", "last_name")
        USER_CHOICES2 = [i for i in user_query]
        context = super().get_context_data(*args, **kwargs)
        context["users_list"] = USER_CHOICES2
        #context["object_list"] = Entry.objects.all().order_by("date_for")
        return context
    
    def get_queryset(self):
        object_list = Entry.objects.all().order_by("date_for")
        return [i for i in object_list if i.is_old == False]

def EntryListView2(request):
    object_list_raw = Entry.objects.all().order_by("date_for")
    
    object_list = [i for i in object_list_raw if i.is_old == False]
    print("POIST", object_list)
    user_query = User.objects.values_list("first_name", "last_name")
    USER_CHOICES2 = [i for i in user_query]
    template = "diary/list_entries.html"
    
    paginator = Paginator(object_list, 2)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    return render(request, template, {"today": today, "object_list": page_obj,
                                      "users_list": USER_CHOICES2})

def searching(request):
    ##users_list = user_choice_inits()
    user_query = User.objects.values_list("first_name", "last_name")
    USER_CHOICES2 = [i for i in user_query]
    users_list = [i for i in USER_CHOICES2]
    query_s = request.POST.get("term_search")
    query_u = request.POST.get("sort_user")
    if query_u == None:
        print("LAUGHTER!!!!!!")
        query_u = ""
    if query_u == "":
        print("MORE LAUGHTER!!!!!")
    
    print(type(query_s))
    print(type(query_u))
    
    
    raw_query_d = request.POST.get("by_date")
    print(type(raw_query_d))
    print("FEEDER!", raw_query_d, type(raw_query_d))


    print("HOOHOOHOOHOO!", type(raw_query_d))
    
    if "query_d" not in request.COOKIES:
        if raw_query_d != "":
            query_d = convert_date(raw_query_d)
            print("PLASS!!!")
        elif raw_query_d == "":
            print("DROGUE!")
            query_d = ""
        else:
            query_d = ""
    else:
        query_d = ""
    
    print("query_u is now a ", type(query_u) , query_u)        
    query_s = cookie_help(request.COOKIES, "query_s", query_s)
    query_u = cookie_help(request.COOKIES, "query_u", query_u)
    query_d = cookie_help(request.COOKIES, "query_d", query_d)
    print("You're a ", query_u)
    
    
    if request.method == "POST" or "query_s" in request.COOKIES:
            
        query_s = change_help(request.method, request.COOKIES, "query_s", query_s, request.POST.get("term_search"), "")
        #query_u = change_help(request.method, request.COOKIES, "query_u", query_u, request.POST.get("sort_user"), "")
        
        if "query_u" in request.COOKIES:
            query_u = user_change_help(request.COOKIES, "query_u", request.POST.get("sort_user"), request.method, query_u, request.COOKIES["query_u"])
        
# # # # # # #         if "query_u" in request.COOKIES:
# # # # # # #             if request.COOKIES["query_u"] == "" and type(request.POST.get("sort_user")) == None:
# # # # # # #                 query_u = "PLOT"
# # # # # # #                 print("ONE")
# # # # # # #             elif request.COOKIES["query_u"] != request.POST.get("sort_user") and request.POST.get("sort_user") == None:
# # # # # # #                 #query_u = request.POST.get("query_u")
# # # # # # #                 #query_u = request.COOKIES["query_u"]
# # # # # # #                 if request.method == "POST":
# # # # # # #                     query_u = ""
# # # # # # #                     print("TWO A")
# # # # # # #                 else:
# # # # # # #                     query_u = request.COOKIES["query_u"]
# # # # # # #                     print("TWO B")
# # # # # # #             elif request.COOKIES["query_u"] != request.POST.get("sort_user") and type(request.POST.get("sort_user")) == str and len(request.POST.get("sort_user")) > 0:
# # # # # # #                 query_u = request.POST.get("sort_user")
# # # # # # #                 print("THREE")
# # # # # # #             elif request.method == "POST" and type(request.POST.get("sort_user")) != request.COOKIES["query_u"]:
# # # # # # #                 if type(request.POST.get("sort_user")) == None:
# # # # # # #                     query_u = ""
# # # # # # #                     print("FOUR")
# # # # # # #                 else:
# # # # # # #                     query_u = request.POST.get("sort_user")
# # # # # # #                     print("FIVE")
# # # # # # #             else:
# # # # # # #                 #query_u = request.COOKIES["query_u"]
# # # # # # #                 query_u = ""
# # # # # # #                 print("SIX")
        print("LASSO", query_u)
        
        
        
        
        
        if "query_u" in request.COOKIES:
            #if request.COOKIES["query_u"] == "None":
            print("POLDARK!", query_u, type(query_u))
                
        else:
            #query_u == "":
            print("PLARKO!", query_u, type(query_u))
            
                
        
        if "query_u" in request.COOKIES:
            print("query_u", request.COOKIES["query_u"])
        
        print("GOOOOOOOOOOOOOVE", request.POST.get("sort_user"))
        print("WARM WARM TOWN!", query_d)
        if request.POST.get("by_date") == "":
            query_d = ""
        elif "query_d" in request.COOKIES and request.POST.get("by_date"):
            if convert_date(request.POST.get("by_date")) != request.COOKIES["query_d"]:
                query_d = convert_date(request.POST.get("by_date"))
                print("ONE", query_d)
            else:
                query_d = request.COOKIES["query_d"]
                print("TWO")
        elif "query_d" in request.COOKIES and not request.POST.get("by_date"):
            if request.COOKIES["query_d"] == "":
                query_d = ""
            else:
                query_d = convert_date(request.COOKIES["query_d"])
            print("THREE")
        elif "query_d" not in request.COOKIES and request.POST.get("by_date") != "":
            query_d = convert_date(request.POST.get("by_date"))
            print("FOUR")
        else:
            query_d = ""
            print("FIVE")
        
        
        
        #if query_type( == 
        
        
        
        
        #query_d = change_help(request.COOKIES, "query_d", query_d, request.POST.get("by_date"))
        print("QUERY_D NOW????????", query_d)
        
        #print("BOOST!")
        #query_d = convert_date(request.COOKIES["query_d"])
                
        print("RAN A LONG LONG", type(query_s))
                
        if query_s != "" or type(query_s) != None:
            que1=Entry.objects.filter(detail__icontains=query_s).order_by("date_for")
            print("GLASS!")
        else:
            que1=Entry.objects.all().order_by("date_for")
            
        if query_u and query_u != None:
            que2 = que1.filter(user__exact=query_u).order_by("date_for")
        else:
            que2 = que1
            print("GLASS2", query_u, type(query_u))
        if query_d != "":
            que3 = que2.filter(date_for__exact=query_d).order_by("user", "title")
        elif query_s != "" or query_u != None:
            que3 = que2
        elif query_s == "" and query_u == "" and query_d == "":
            que3 = Entry.objects.none()
        else:
            que3 = Entry.objects.none()
    
    
    if len(que3) == 0:
        searcho = "EMPTY!"
    else:
        searcho = "SEARCHING!"
    saved = ""
    
    
    
    print("PANPANPANPAN!", len(que3), type(que3))
    que3 = [i for i in que3]
    print("HESPY!", type(que3))
    
    #Pagination
    paginator = Paginator(que3, 2)
    print(paginator)
    page_number = request.GET.get("page")
    print(page_number)
    page_obj = paginator.get_page(page_number)
# #     try:
# #         page_obj = paginator.page(1)
# #     except PageNotAnInteger:
# #         page_obj = paginator.page(page)
# #     except EmptyPage:
# #         page_obj = paginator.page(paginator.num_pages)
        
    print("MOST!!", query_u, type(query_u))
    response =  render(request, "diary/list_entries.html", {"searchu": searcho, "object_list": page_obj,
                                                        "today": today, "users_list": USER_CHOICES2,
                                                       "word_query": query_s, "user_query": query_u,
                                                       "date_query": query_d, "saved": saved,
                                                       "page_obj": page_obj, })
    response.set_cookie("query_s", query_s)
    response.set_cookie("query_u", query_u)
    print(query_u, type(query_u), "GUSPY!")
    response.set_cookie("query_d", query_d)
    
    return response

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
# #     return render(request, template, {"searchu": searcho, "object_list": quer_user,
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
    
    
    paginator = Paginator(cleared_query, 2)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    response = render(request, template, {"searchu": searcho, "object_list": page_obj,
                                        "today": today, "users_list": USER_CHOICES2,
                                      "saved": saved,})
    #return HttpResponseRedirect(reverse("diary:home"))
    
    cookoes = ["query_s", "query_u", "query_d"]
    for i in cookoes:
        response.delete_cookie(i)
    

    
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
    
# # def UpdateEntryView2(request):
# #     form = UpdateViewForm
# #     template = "diary/edit_entry.html"
# #     pk = request.GET.get("pk")
# #     return render(request, template, {"form":form, "pk":pk})

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
        return render(request, "diary/new_entry.html", {"today": today, "users_list": USER_CHOICES2})

def UpdateEntryView2(request, pk):
    #form = request.POST.get("ebbo")
    #form = UpdateViewForm()
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
        #if form.is_valid():
#         for i in (title, detail, user, date):
#             print(i)
        the_entry.title = title
        the_entry.detail = detail
        the_entry.user = user
        the_entry.mod_by = request.user.first_name
        the_entry.date_for = convert_date(date)
        the_entry.last_modified = convert_date(date)
        #the_entry.title.save()
        print("Beeeeooorp", the_entry.date_for)
        the_entry.save()
        saved = "PENCE!"
        all_entries = Entry.objects.all().order_by("date_for")
        messages.success(request, "Entry updated!")
        return HttpResponseRedirect(reverse("diary:home"))
#         render(request, "diary/list_entries.html", {"saved": saved, "object_list": all_entries,
#                                                     "users_list": USER_CHOICES2})


#     else:
#         saved = None
    
    #the_entry.save()
    
    print("BEENCE")
    template = "diary/edit_entry.html"
    shit = "shit!"
    return render(request, template, {"title": title, "detail": detail,
                                      "user": user, "date": date,
                                      "entry": the_entry, "shit": shit,
                                      "users_list": USER_CHOICES2,
                                      "selected_user": the_entry.user})
            
        

class UpdateEntryView(LoginRequiredMixin, UpdateView):
    model = Entry
# # #     fields = ("title",
# # #               "detail",
# # #               "user",
# # #               "date_for")
    form_class = UpdateViewForm
    #form_class()
    #form = form_class()
    extra_context = {"form":form_class}
    #user_query = User.objects.values_list("first_name", "last_name")
    template_name = "diary/edit_entry.html"
    
# # #     class Meta:
# # #         model = Entry
# # #         fields = ("title",
# # #               "detail",
# # #               "user",
# # #               "date_for")
#         widgets = {
#             "": forms.Choice}
    
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
    return render(request, template, {"object_list": all_entries, "users_list": users_list, 
                                      "today": today, "saved": saved, "searchu": searcho})
    
def search_all(request):
    all_entries = Entry.objects.all().order_by("date_for")
    user_query = User.objects.values_list("first_name", "last_name")
    USER_CHOICES2 = [i for i in user_query]
    searcho = "SEARCHING!"
    template = "diary/list_entries.html"
    return render(request, template, {"object_list": all_entries, "users_list": USER_CHOICES2,
                                      "all_query": "ALL!", "today": today, "searchu": searcho,
                                      "word_query": "", "user_query": None, "date_query": ""})

# class HomePageView(TemplateView):
#     template_name = "diary/home2.html"
        
# def hello(request):
#     plinth = "Yaroo"
#     bup = [1,2,3,4,5]
#     response = render(request, "diary/index.html", {"plinth": plinth, "bup": bup})
#     return response

