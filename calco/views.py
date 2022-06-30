from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .calc_time import main as calculation
from .models import Colour


# Create your views here.

def swappy(i):
    if i == "x":
        return "*"
    elif i == "÷":
        return "/"
    elif i == "CLEAR":
        return "C"
    else:
        return i

def cooko(request, clicked_input):
    clicked_input = swappy(clicked_input)
    signs = ["+", "-", "*", "/", "(", ")"]
    signs2 = ["*", "/"]
    if not "sum_list" in request.COOKIES:
        sum_list = request.COOKIES.get("sum_list", "")
    else:
        
        sum_list = request.COOKIES["sum_list"].split(",")
        
        print(sum_list)
        sum_list = [i for i in sum_list[0]]
        sum_list.append(str(clicked_input))
        print("GARCEY!!!!!", sum_list[-1])

        print(sum_list, type(sum_list))
        sum_list = "".join(sum_list)
    try:
        if len(sum_list) > 1:
            if sum_list[-2] in signs2 and sum_list[-1] in signs2:
                sum_list = sum_list[:-1]
            elif sum_list[-1] in signs2 and sum_list[-2] == "-" or sum_list[-1] in signs2 and sum_list[-2] == "+":
                sum_list = sum_list[:-1]
            elif len(sum_list) >= 4 and sum_list[-3] in signs and sum_list[-2] == "0" and type(eval(sum_list[-1])) == int:
                print("PANS!!!")
                sum_list = sum_list[:-2] + sum_list[-1]
            elif len(sum_list) == 2 and sum_list[0] == "0" and type(eval(sum_list[1])) == int:
                sum_list = sum_list[1]
    except SyntaxError or NameError:
        sum_list = "0"
        
            
    return sum_list

def calc_prep(sum_list):
    signs = ["+", "-", "*", "/", "."]
    brackets = ["(", ")"]
    if len(sum_list) > 2 and sum_list[-1] in signs and sum_list[-1] == ".":
        to_calc = str(sum_list[:-1])
    elif len(sum_list) >= 2 and sum_list[-1] in signs:
        if "(" in sum_list and ")" not in sum_list:
            #total000 = str(eval(sum_list[:-1] + ")"))
            to_calc = str(sum_list[:-1] + ")")
        else:
            print("POCKEY", sum_list[:-1])
            to_calc = str(sum_list[:-1])
    elif len(sum_list) == 2 and sum_list[-1] in signs:
        print("POCKEY2", sum_list[:-1])
        to_calc = str(sum_list[:-1])
    elif len(sum_list) > 2 and sum_list[-2] in signs and sum_list[-1] in brackets:
        to_calc = str(sum_list[:-2])
    elif len(sum_list) > 2 and sum_list[-2] == brackets[1] and sum_list[-1] in signs:
        to_calc = str(sum_list[-1])
    elif "(" in sum_list and ")" not in sum_list:
        if sum_list[-1] in signs:
            print("PI", sum_list[:-1] + ")")
            to_calc = str(sum_list[:-1] + ")")
        else:
            to_calc = str(sum_list + ")")
    else:
        to_calc = str(sum_list)
    return to_calc

def no_zero(num):
    if num[0] == "0":
        return num[1:]
    else:
        return num

def num_disp(sum_list):
    signs = ["+", "-", "*", "/", "(", ")"]
    dispo = []
    if len(sum_list) == 1:
        return sum_list
    elif len(sum_list) > 1:
        for i in reversed(sum_list):
            dispo.append(i)
            if dispo[-1] in signs:
                print("PINCERS", "".join(reversed(dispo[:-1])))
                return "".join(reversed(dispo[:-1]))
                #return no_zero(num)
        
        return "".join(reversed(dispo))
    else:
        #return "0"
        return ""

def calc1(request):
#     if not "design" in request.COOKIES:
#         picked = "#ffffff"
    if "design" in request.COOKIES:
        calc_num = request.COOKIES["design"]
    else:
        calc_num = "1"
    if "picked_colour" in request.COOKIES:
        picked_colour = request.COOKIES["picked_colour"]
    else:
        picked_colour = "#ffffff"
    print("R&j / r&d", calc_num)
    template = "calco/calc{}.html".format(calc_num)
#     buttons = ["CLEAR", "1", "2", "3", "+", "4", "5", "6", "-", "7", "8",\
#                "9", "x", "0", ".", "÷","(", ")", "="]
    buttons = ["CLEAR", "1", "2", "3", "+", "4", "5", "6", "-", "7", "8", "9", "x", \
               "(", ")", ".", "÷", "="]
#     ends = ["+","-","x","÷", "CLEAR"]
    ends = ["CLEAR", "÷"]
    signs = ["+", "-", "*", "/", "(", ")"]
    colours = Colour.objects.values_list("colour_name", "colour_hex")
    colours_list = [i for i in colours]

    if "sum_list" in request.COOKIES:
        final_list = request.COOKIES["sum_list"]

        #total = "0"
        #final_list = sum_list
        if len(final_list) > 0 and final_list[-1] == "=":
            try:
                total = str(eval(calc_prep(final_list[:-1])))
            except SyntaxError or NameError:
                #total = "ERROR"
                total = "0"
            if total[-2:] == ".0":
                total = str(total[:-2])
            cooky = total
            response = render(request, template, {"buttons": buttons, \
                                                  "ends": ends, "screen": total, \
                                                  "colours_list": colours_list, "picked_colour": picked_colour})
            response.set_cookie("sum_list", cooky)
            return response
        elif len(final_list) > 1 and final_list[-1] == "C" or len(final_list) == 1 and final_list[0] == "C":
            final_list = ""
            total = ""
            
            print("DIRE STRAITS", total)
            cooky = total
            response = render(request, template, {"buttons": buttons, \
                                                  "ends": ends, "screen": total, \
                                                  "colours_list": colours_list, "picked_colour": picked_colour})
            
            response.set_cookie("sum_list", cooky)
            return response
        
        elif len(final_list) > 0:
            if final_list[-1] in signs:
                total = final_list[-1]
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
    
    response = render(request, template, {"buttons": buttons, "ends": ends, \
                                          "screen": total, "colours_list": colours_list, \
                                          "picked_colour": picked_colour})
    cooky = cooko(request, "")
    #response.delete_cookie("sum_list")
    response.set_cookie("sum_list", cooky)
    print("BIA", total)
    return response

def one(request):
    num = request.GET.get("num_id")
    print(num)
    cooky = cooko(request, num)
    response = HttpResponseRedirect(reverse("calco:calc1"))
    response.set_cookie("sum_list", cooky)
    return response

def first(request):
    if "design" in request.COOKIES:
        templ8 = request.COOKIES["design"]
#     else:
    templ8 = request.GET.get("templ8", "1")
#         print("PRUCE!", templ8)
    
    if "picked_colour" in request.COOKIES:
        picked = request.COOKIES["picked_colour"]
    else:
        picked = "#ffffff"
    #cooky = cooko(request, templ8)
    print("GRUZE", templ8)
    response = HttpResponseRedirect(reverse("calco:calc1"))
    response.set_cookie("design", templ8)
    response.set_cookie("picked_colour", picked)
    return response

def banty(request):
    return HttpResponseRedirect(reverse("calco:calc1"))

def colour_pick(request):
#     if request.method == "POST":
#         if form.is_valid():
    colour = request.GET.get("coloury")
    if colour:
        colour = colour
        print("JANT", colour)
#     else:
#         colour = "#ffffff"
#     colour = request.POST.get("coloury", "JOFF")
#     print("pranty!", colour)
    response = HttpResponseRedirect(reverse("calco:calc1"))
    response.set_cookie("picked_colour", colour)
    return response
