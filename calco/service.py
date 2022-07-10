from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Colour

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
        print("CLICKED", type(clicked_input))
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
            elif len(sum_list) >= 4 and sum_list[-3] in signs and sum_list[-2] == "0" and sum_list[-1].isdigit():
                print("PANS!!!")
                sum_list = sum_list[:-2] + sum_list[-1]
            elif len(sum_list) == 2 and sum_list[0] == "0" and sum_list[1].isdigit():
                sum_list = sum_list[1]                
    except (SyntaxError, NameError) as e:
        sum_list = "ERROR"
    return sum_list

def calc_prep(sum_list):
    signs = ["+", "-", "*", "/", "."]
    brackets = ["(", ")"]
    if len(sum_list) > 2 and sum_list[-1] in signs and sum_list[-1] == ".":
        to_calc = str(sum_list[:-1])
    elif len(sum_list) >= 2 and sum_list[-1] in signs:
        if "(" in sum_list and ")" not in sum_list:
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
        return "".join(reversed(dispo))
    else:
        return ""

def cookie_default(name, rc, default):
    if name in rc:
        return rc[name]
    else:
        return default

def cookie_eater(reqc, resp):
    cookie_list = ["namey", "boxo", "bisp", "chosen", "risp", "filtery", "sesho", "cou", "startytime", \
              "finishy_time", "excepor", "resety", "squores", "goesy", "query_s", "query_u", "query_d"]
    for i in cookie_list:
        if i in reqc:
            resp.delete_cookie(i)

def font_sizer(total):
    if len(total) < 19:
        return "40px"
    else:
        return "24px"
