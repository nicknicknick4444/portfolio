import datetime as datetime_module
from crontab import CronTab
from datetime import datetime
from .email_send import main as email_main
from .models import Entry, User

user_query = User.objects.values_list("first_name","last_name")
USER_CHOICES = [i for i in user_query]

def convert_date(d):
# #     datey_conv =
    return datetime.strptime(d, "%Y-%m-%d").date()
# #     print("YOOOO!", datey_conv, type(datey_conv))
# #     return datey_conv

def convert_date2(d):
    print("PORTY!", d, type(d))
    converted = d.strftime("%d/%m/%Y")
    print(converted)
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
            print("PRINTING", orig, reqc[name], type(orig), type(reqc[name]))
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
            print("PRADY!!!!!!!!!!")
            return reqc[name]
        else:
            return orig
    elif name in reqc:
        return reqc[name]

    else:
        return var
    #return var

def user_change_help(reqc, name, orig, reqm, reqcname):
    #if name in reqc:
    if reqc[name] == "" and type(orig) == None:
        print("ONE!!")
        return "PLOT"
        
    elif reqc[name] != orig and orig == None:
        #query_u = request.POST.get("query_u")
        #query_u = request.COOKIES["query_u"]
        if reqm == "POST":
            print("TWO A!!")
            return ""
            
        else:
            print("TWO B!!")
            return reqc[name]
            
    elif reqc[name] != orig and type(orig) == str and len(orig) > 0:
        print("THREE!!")
        return orig
        
    elif reqm == "POST!!" and type(orig) != reqc[name]:
        if type(orig) == None:
            print("FOUR!!")
            return ""
            #print("FOUR")
        else:
            print("FIVE A!!")
            return orig
            #print("FIVE")
    elif orig == reqc[name]:
        print("FIVE B!!")
        return reqc[name]
    else:
        print("SIX!!")
        #query_u = request.COOKIES["query_u"]
        return ""
        #print("SIX")
# #     else:
# #         print("SEVEN!!")
# #         return orig

def date_change_help(reqc, name, orig):
    # Start of query_d help
    if orig == "":
        return ""
    elif name in reqc and orig:
        if convert_date(orig) != reqc[name]:
            return convert_date(orig)
            print("ONE", query_d)
        else:
            return reqc[name]
            print("TWO")
    elif name in reqc and not orig:
        if reqc[name] == "":
            return ""
        else:
            return convert_date(reqc[name])
        print("THREE")
    elif name not in reqc and orig != "":
        return convert_date(orig)
        print("FOUR")
    else:
        return ""
        print("FIVE")
    # End of query_d help


def filter_func(query_s, query_u, query_d):
    if query_s != "" or type(query_s) != None or query_s != None:
        que1 = Entry.objects.filter(detail__icontains=query_s).order_by("date_for", "user", "title")
        #print("ONE!", que1)
    else:
        que1 = Entry.objects.all().order_by("date_for", "user")
        #print("TWO!", que1)
        
    if query_u and query_u != "":
        que2 = que1.filter(user__exact=query_u).order_by("date_for", "user", "title")
        #print("THREE!", que2)
    else:
        que2 = que1
        #print("FOUR!", que2)
    if query_d != "":
        return que2.filter(date_for__exact=query_d).order_by("user", "title")
        #print("FIVE!", que3)
    elif query_s != "" or query_u != "":
        return que2
        #print("SIX!", que3)
    elif query_s == "" and query_u == "" and query_d == "":
        return Entry.objects.none()
        #print("SEVEN!", que3)
    else:
        return Entry.objects.none()
        #print("EIGHT!", que3)

def today():
    return datetime_module.datetime.now().date()

# # # # def cronny():
# # # # # #     # Use root user
# # # # # #     cron = CronTab(user="root")
# # # #     
# # # #     #Use the current user
# # # #     my_cron = CronTab(user=True)
# # # #     
# # # #     # Creting an object from the clas sinto a file
# # # #     file_cron = CronTab(tabfile="filename.tab")
# # # #     
# # # #     # Create new job
# # # #     job = cron.new(command=email_main())
# # # #     
# # # #     # Setting restrictions of jobule
# # # #     
# # # #     # Job on 1st - 5th days of the week
# # # #     job.day.on(1,2,3,4,5)
    
    #Clearing 
    
    

