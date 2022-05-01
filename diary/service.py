from datetime import datetime
from .models import User

def convert_date(d):
    datey_conv = datetime.strptime(d, "%Y-%m-%d").date()
    print("YOOOO!", datey_conv, type(datey_conv))
    return datey_conv

user_query = User.objects.values_list("first_name","last_name")
USER_CHOICES = [i for i in user_query]

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
