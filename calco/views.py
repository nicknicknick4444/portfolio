from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Colour
from .service import swappy, cooko, calc_prep, num_disp, cookie_default, cookie_eater


# Create your views here.

def key_process(request):
    response = HttpResponseRedirect(reverse("calco:calc1"))
    num = request.GET.get("num_id")
    if request.COOKIES["sum_list"] == "MEMORY ERROR" and num != "CLEAR":
        return response
    else:
        #if request.COOKIES["design"] == "" or "design" not in request.COOKIES:
        if len(request.COOKIES["sum_list"]) <= 17 or num == "CLEAR":
            print(num)
            cooky = cooko(request, num)
            response.set_cookie("sum_list", cooky)
            
            return response
        elif len(request.COOKIES["sum_list"]) > 17 and num != "CLEAR":
            response.set_cookie("sum_list", "MEMORY ERROR")
            return response
        else:
            return response
    
def calc1(request):    
    templ8 = cookie_default("design", request.COOKIES, "1")
    picked_colour = cookie_default("picked_colour", request.COOKIES, "#D6DBDF")
    
    print("R&j / r&d", templ8)
    template = "calco/calc{}.html".format(templ8)
    buttons = ["CLEAR", "1", "2", "3", "+", "4", "5", "6", "-", "7", "8", "9", "x", "0", \
               "(", ")", "÷", ".", "="]
    signs = ["+", "-", "*", "/", "(", ")"]
    colours = Colour.objects.values_list("colour_name", "colour_hex")
    colours_list = [i for i in colours]
    
    if "sum_list" in request.COOKIES:
        final_list = request.COOKIES["sum_list"]
        
        if len(final_list) > 0 and final_list[-1] == "C":
            print("TUBES", final_list[-1])
            final_list = ""
            total = ""
            cooky = total
            response = render(request, template, {"buttons": buttons, "screen": total, \
                                                 "colours_list": colours_list, "picked_colour": picked_colour})
            response.set_cookie("sum_list", cooky)
            response.set_cookie("design", templ8)
            response.set_cookie("picked_colour", picked_colour)
            cookie_eater(request.COOKIES, response)
            return response
        elif len(final_list) > 0 and final_list[-1] == "=":
            print("YAAAAAAARGH!!!!")
            try:
                total = str(eval(calc_prep(final_list[:-1])))
                print("Miss Burfield")
            except (SyntaxError, NameError) as e:                    
                print("CLAGGY")
                total = "ERROR"
                #total = "0.0"

            if total[-2:] == ".0":
                total = str(total[:-2])
            elif "." in total and total[-2:] != ".0" and len(total) > 14:
                five = total[:5]
                if "." in five:
                    print("PIES OF PEACE")
                    print(type(total))
                    total = float(total)
                    total = "{:.7f}".format(total)
                else:
                    total = total
        
            cooky = total
            response = render(request, template, {"buttons": buttons, "screen": total, \
                                                  "colours_list": colours_list, "picked_colour": picked_colour})
            response.set_cookie("sum_list", cooky)
            response.set_cookie("design", templ8)
            response.set_cookie("picked_colour", picked_colour)
            cookie_eater(request.COOKIES, response)
            return response
        elif len(final_list) > 1 and final_list[-1] == "C":
            final_list = ""
            total = ""
        elif len(final_list) == 1 and final_list[0] == "C":
            final_list = ""
            total = ""
        elif len(final_list) == 6 and final_list[:-1] == "ERROR":
            final_list = final_list[-1]
            total = final_list
            
            print("DIRE STRAITS", total)
            
            cooky = total
            response = render(request, template, {"buttons": buttons, "screen": total, \
                                                  "colours_list": colours_list, "picked_colour": picked_colour})
            
            response.set_cookie("sum_list", cooky)
            response.set_cookie("design", templ8)
            response.set_cookie("picked_colour", picked_colour)
            cookie_eater(request.COOKIES, response)
            return response
        
        elif len(final_list) > 0:
            if final_list[-1] in signs:
                total = final_list[-1]
#             elif final_list[-1] == "0" and final_list[-2] in signs:
#                     print("TLAD!")
#                     total = ""
            # FUNCO HERE
            else:
                print()
                total = num_disp(final_list)
        elif len(final_list) == 1:
            total = str(final_list)
        else:
            total = final_list
    else:
        total = ""
    
    response = render(request, template, {"buttons": buttons, "screen": total, \
                                          "colours_list": colours_list, "picked_colour": picked_colour})
    cooky = cooko(request, "")
    response.set_cookie("sum_list", cooky)
    response.set_cookie("design", templ8)
    response.set_cookie("picked_colour", picked_colour)
    cookie_eater(request.COOKIES, response)
    print("BIA", total)
    return response
    
def first(request):
    if "design" in request.COOKIES:
        templ8 = request.COOKIES["design"]
    templ8 = request.GET.get("templ8", "1")    
    if "picked_colour" in request.COOKIES:
        picked = request.COOKIES["picked_colour"]
    else:
        picked = "#D6DBDF"
    print("GRUZE", templ8)
    response = HttpResponseRedirect(reverse("calco:calc1"))
    response.set_cookie("design", templ8)
    response.set_cookie("picked_colour", picked)
    return response

def colour_pick(request):
    pick = request.GET.get("coloury")
    if "picked_colour" in request.COOKIES:
        if pick == "":
            colour = request.COOKIES["picked_colour"]
            print("STAYS", colour)
        elif pick != "":
            colour = pick
            print("PICKED!", colour)
        else:
            colour = "#D6DBDF"
            print("JANT!", colour)
    else:
        if pick:
            colour = pick
        else:
            colour = "#D6DBDF"
    response = HttpResponseRedirect(reverse("calco:calc1"))
    response.set_cookie("picked_colour", colour)
    return response
