from .service import api_call, make_id, cookie_help1, cookie_help2, time_check, make_lists, cleanup_cookies

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
import ast, datetime, json
from datetime import datetime, timedelta


# Create your views here.

api_key = "b2bf55e4a6c24c55abe104821222603"

# https://www.weatherapi.com/

def subbo(request):
    response = HttpResponseRedirect(reverse("plp:index"))
    done = "done"

    nowy = datetime.now()
    searching = cookie_help1(request.COOKIES, "searched", done)
    time_stamp = cookie_help1(request.COOKIES, "time_stamp", nowy)

    response.set_cookie("searched", searching)
    response.set_cookie("time_stamp", nowy)

    return response
    
def poy(request):
    my_sesh = cookie_help1(request.COOKIES, "my_sesh", make_id())
    right_now = datetime.now()
    if "time_stamp" in request.COOKIES:
        the_time = datetime.strptime(request.COOKIES["time_stamp"], "%Y-%m-%d %H:%M:%S.%f")
    else:
        the_time = datetime.now()
    timefunc = time_check("time_stamp", request.COOKIES, right_now, the_time, timedelta(minutes=100))

    if "searched" in request.COOKIES:
        if "goody" not in request.COOKIES:            
            collgood, collbad = make_lists()
            goody = cookie_help2(request.COOKIES, "goody", collgood)
            baddy = cookie_help2(request.COOKIES, "baddy", collbad)
        elif timefunc:
            nowy = datetime.now()
            time_stamp = cookie_help1(request.COOKIES, "time_stamp", nowy)
            collgood, collbad = make_lists()
            goody = cookie_help1(request.COOKIES, "goody", collgood)
            baddy = cookie_help1(request.COOKIES, "baddy", collbad)
            gus = "Yes"    
        else:
            collgood = ast.literal_eval(request.COOKIES["goody"])
            collbad = ast.literal_eval(request.COOKIES["baddy"])
        response = render(request, "plp/index.html", {"best":collgood, "worst":collbad,
                            "g1top": int(collgood[0][3][0]), "g1left": int(collgood[0][3][1]),
                            "g2top": int(collgood[1][3][0]), "g2left": int(collgood[1][3][1]),
                            "g3top": int(collgood[2][3][0]), "g3left": int(collgood[2][3][1]),
                            "g4top": int(collgood[3][3][0]), "g4left": int(collgood[3][3][1]),
                            "g5top": int(collgood[4][3][0]), "g5left": int(collgood[4][3][1]),
                            "b1top": int(collbad[0][3][0]), "b1left": int(collbad[0][3][1]),
                            "b2top": int(collbad[1][3][0]), "b2left": int(collbad[1][3][1]),
                            "b3top": int(collbad[2][3][0]), "b3left": int(collbad[2][3][1]),
                            "b4top": int(collbad[3][3][0]), "b4left": int(collbad[3][3][1]),
                            "b5top": int(collbad[4][3][0]), "b5left": int(collbad[4][3][1])}
                          )
        cleanup_cookies(request, response)
        if not "my_sesh" in request.COOKIES:
            response.set_cookie("my_sesh", make_id())
        response.set_cookie("goody", collgood)
        response.set_cookie("baddy", collbad)
        if timefunc:
            response.set_cookie("time_stamp", nowy)
    else:
        response =  render(request, "plp/index.html", {})
    return response
