from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .calc_time import main as calculation
from .models import Colour
from .service import swappy, cooko, calc_prep, num_disp, key_process, first, colour_pick


# Create your views here.


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
    buttons = ["CLEAR", "1", "2", "3", "+", "4", "5", "6", "-", "7", "8", "9", "x", "0", \
               "(", ")", "÷", ".", "="]
#     ends = ["+","-","x","÷", "CLEAR"]
    ends = ["CLEAR", "÷"]
    signs = ["+", "-", "*", "/", "(", ")"]
    colours = Colour.objects.values_list("colour_name", "colour_hex")
    colours_list = [i for i in colours]

    if "sum_list" in request.COOKIES:
        final_list = request.COOKIES["sum_list"]

        #total = "0"
        #final_list = sum_list
        
        if len(final_list) > 0 and final_list[-1] == "C":
            print("TUBES", final_list[-1])
            final_list = ""
            total = ""
            cooky = total
            response = render(request, template, {"buttons": buttons, "ends": ends, "screen": total, \
                                                 "colours_list": colours_list, "picked_colour": picked_colour})
            response.set_cookie("sum_list", cooky)
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
#             if total[-1] == "0":
#                 total = ""
#         elif len(final_list) >= 3 and final_list[-2:] == "+0":
#             print("POGGY!")
#             final_list = ast.literal_eval(final_list[:-2])
#         elif len(final_list) >= 3 and final_list[-2:] == "-0":
#             final_list = ast.lieral_evalfinal_list[:-2]
#             print("KWOGGY")
        
        
            cooky = total
            response = render(request, template, {"buttons": buttons, \
                                                  "ends": ends, "screen": total, \
                                                  "colours_list": colours_list, "picked_colour": picked_colour})
            response.set_cookie("sum_list", cooky)
            return response
        elif len(final_list) > 1 and final_list[-1] == "C":
            final_list = ""
            total = ""
        elif len(final_list) == 1 and final_list[0] == "C":
            final_list = ""
            total = ""
#         elif "C" in final_list:
#             final_list = ""
#             total = ""
        elif len(final_list) == 6 and final_list[:-1] == "ERROR":
            final_list = final_list[-1]
            total = final_list
            
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
    
    response = render(request, template, {"buttons": buttons, "ends": ends, \
                                          "screen": total, "colours_list": colours_list, \
                                          "picked_colour": picked_colour})
    cooky = cooko(request, "")
    response.set_cookie("sum_list", cooky)
    print("BIA", total)
    return response

