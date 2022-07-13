import datetime as datetime_module
from datetime import datetime
from .email_send import main as email_main
from .models import Entry, User

user_query = User.objects.values_list("first_name","last_name")
USER_CHOICES = [i for i in user_query]

def convert_date(d):
    return datetime.strptime(d, "%Y-%m-%d").date()

def convert_date2(d):
    converted = d.strftime("%d/%m/%Y")
    return converted

def cookie_help(reqc, name, func):
    if name not in reqc:
        var = reqc.get(name, func)
    else:
        var = reqc[name]
    return var

def search_change_help(rm, reqc, name, orig, var):
    if rm == "POST":
        if name in reqc:
            if orig != reqc[name]:
                return orig
            else:
                return reqc[name]
        elif name not in reqc:
            if orig == "":
                return ""
            elif orig == None:
                return ""
            else:
                return orig
        elif orig == reqc[name]:
            return reqc[name]
        else:
            return orig
    elif name in reqc:
        return reqc[name]
    else:
        return var

def user_change_help(reqc, name, orig, reqm, reqcname):
    if reqc[name] == "" and type(orig) == None:
        return ""
        
    elif reqc[name] != orig and orig == None:
        if reqm == "POST":
            return ""
            
        else:
            return reqc[name]
            
    elif reqc[name] != orig and type(orig) == str and len(orig) > 0:
        return orig
        
    elif reqm == "POST!!" and type(orig) != reqc[name]:
        if type(orig) == None:
            return ""
        else:
            return orig
    elif orig == reqc[name]:
        return reqc[name]
    else:
        return ""

def date_change_help(reqc, name, orig):
    if orig == "":
        return ""
    elif name in reqc and orig:
        if convert_date(orig) != reqc[name]:
            return convert_date(orig)
        else:
            return reqc[name]
    elif name in reqc and not orig:
        if reqc[name] == "":
            return ""
        else:
            return convert_date(reqc[name])
    elif name not in reqc and orig != "":
        return convert_date(orig)
    else:
        return ""

def filter_func(query_s, query_u, query_d):
    if query_s != "" or type(query_s) != None or query_s != None:
        que1 = Entry.objects.filter(detail__icontains=query_s).order_by("date_for", "user", "title")
    else:
        que1 = Entry.objects.all().order_by("date_for", "user")
        
    if query_u and query_u != "":
        que2 = que1.filter(user__exact=query_u).order_by("date_for", "user", "title")
    else:
        que2 = que1
    if query_d != "":
        return que2.filter(date_for__exact=query_d).order_by("user", "title")
    elif query_s != "" or query_u != "":
        return que2
    elif query_s == "" and query_u == "" and query_d == "":
        return Entry.objects.none()
    else:
        return Entry.objects.none()

def today():
    return datetime_module.datetime.now().date()

def cookie_eat(reqc, resp):
    mainlist = ["namey", "boxo", "bisp", "chosen", "risp", "filtery", "sesho", "cou", "startytime", \
                "finishy_time", "excepor", "resety", "squores", "goesy", "query_s", \
                "query_u", "query_d", "design", "picked_colour", "sum_list", "colours_list"]
    for i in mainlist:
        if i in reqc:
            resp.delete_cookie(i)
    