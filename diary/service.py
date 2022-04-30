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

def change_help(rm, reqc, name, var, orig, blnk):
    if rm == "POST":
        if name in reqc:
            print("PRINTING", orig, reqc[name], type(orig), type(reqc[name]))
            if orig != reqc[name]:
                var = orig
            else:
                var = reqc[name]
                
        elif name not in reqc:
            if orig == "":
                var = ""
            elif orig == None:
                var = ""
            else:
                var = orig
                
        else:
            var = orig

    elif name in reqc:
        var = reqc[name]

    else:
        var = var
    return var

def user_change_help(reqc, name, orig, reqm, var, reqcname):
        if name in reqc:
            if reqcname == "" and type(orig) == None:
                return "PLOT"
                #print("ONE")
            elif reqcname != orig and orig == None:
                #query_u = request.POST.get("query_u")
                #query_u = request.COOKIES["query_u"]
                if reqm == "POST":
                    return ""
                    #print("TWO A")
                else:
                    return reqcname
                    #print("TWO B")
            elif reqcname != orig and type(orig) == str and len(orig) > 0:
                return orig
                #print("THREE")
            elif reqm == "POST" and type(orig) != reqcname:
                if type(orig) == None:
                    return ""
                    #print("FOUR")
                else:
                    return orig
                    #print("FIVE")
            else:
                #query_u = request.COOKIES["query_u"]
                return ""
                #print("SIX")


