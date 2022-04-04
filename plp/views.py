from .service import api_call, plotto, make_id, cookie_help1, cookie_help2, time_check, make_lists

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
# #     if not "searched" in request.COOKIES:
# #         searching = request.COOKIES.get("searched", done)
# #     else:
# #         searching = request.COOKIES["searched"]
    nowy = datetime.now()
    searching = cookie_help1(request.COOKIES, "searched", done)
    time_stamp = cookie_help1(request.COOKIES, "time_stamp", nowy)

    response.set_cookie("searched", searching)
    response.set_cookie("time_stamp", nowy)

    return response
    

def poy(request):
# #     if not "my_sesh" in request.COOKIES:
# #         my_sesh = request.COOKIES.get("my_sesh", make_id())
# #     else:
# #         my_sesh = request.COOKIES["my_sesh"]
        
        
    my_sesh = cookie_help1(request.COOKIES, "my_sesh", make_id())
    #right_now = datetime.datetime.now(datetime.timezone.utc)
    right_now = datetime.now()
    if "time_stamp" in request.COOKIES:
        the_time = datetime.strptime(request.COOKIES["time_stamp"], "%Y-%m-%d %H:%M:%S.%f")
    else:
        the_time = datetime.now()
    timefunc = time_check("time_stamp", request.COOKIES, right_now, the_time, timedelta(minutes=100))
        
        
        
#     paste = "Yeeeee! Loveable drogue!"
#     endo = []
#     listy = [1,2,3,4,5,6,7,8,9,10]
#     for i in listy:
#         if i%2==0:
#             endo.append("POY!")
            
#     locdict = {"London":(100, 65), "Manchester":(150,100), "Brentwood":(185, 180),
#                "Southend-On-Sea":(195,115), "Chelmsford":(212, 200)}
#     placey = ["London","Manchester","Brentwood","Southend-On-Sea","Chelmsford"]
    #placey = ["London"]
    #placey = ['Wickford', 5.6, 0.0]
#     placey = ["Aberdeen","Bath","Brighton & Hove","Chester","Chelmsford","Stortford","Brentwood","Billericay","Southend-On-Sea","Bristol","Armagh",
#              "Bangor","Belfast","Birmingham","Cambridge","Cantebury","Cardiff","Carlisle","Chichester","Coventry","Derby","Derry",
#              "Dundee","Durham","Edinburgh","Ely","Exeter","Glasgow","Gloucester","Hereford","Inverness","Kingston-Upon-Hull",
#              "Lancaster","Leeds","Leicester","Lichfield","Lincoln","Lisburn","Liverpool","Manchester","Newcastle-Upon-Tyne",
#              "Newport","Newry","Norwich","Nottingham","Oxford","Perth","Peterborough","Plymouth","Portsmouth","Preston","Ripon",
#              "St Albans","St Asaph","St Davids","Salford","Salisbury","Sheffield","Southampton","Stirling","Stoke-on-Trent",
#              "Sunderland","Swansea","Truro","Wakefield","Wells","Wickford","Winchester","Wolverhampton","Worcester","York"]
#     collection = []
#     collgood = []
#     collbad = []
    #response = requests.get("http://api.weatherapi.com/v1/current.json?key=b2bf55e4a6c24c55abe104821222603&q={}".format(placey))
    
    
    if "searched" in request.COOKIES:
        if "goody" not in request.COOKIES:
            
# # # # #             collection = []
# # # # #             collgood = []
# # # # #             collbad = []
# # # # #             for p in placey:
# # # # #                 litoure = []
# # # # #                 response = api_call(p)
# # # # #                 name = response.json()["location"]["name"]
# # # # #                 temp = response.json()["current"]["feelslike_c"]
# # # # #                 rainfall = response.json()["current"]["precip_mm"]
# # # # #                 coord = locdict[p]
# # # # #                 
# # # # #                 litoure.append(name)
# # # # #                 litoure.append(temp)
# # # # #                 litoure.append(rainfall)
# # # # #                 litoure.append(coord)
# # # # #                 collection.append(litoure)
# # # # #                 
# # # # #             coll_proto1 = sorted(collection, key=lambda x: int(x[1]))
# # # # #             print("CLUSE", collection)
# # # # #             print("GRUSE", coll_proto1)
# # # # #             coll_proto2 = sorted(coll_proto1, key=lambda x: int(x[2]))
# # # # #             print("BRUSE", coll_proto2)
# # # # #             collgood = [coll_proto2[-3:]]
# # # # #             collbad = [coll_proto2[:3]]
# # # # #             collgood = [i for i in reversed(collgood[0])]
# # # # #             print("WOW!!", collgood)
# # # # #             collbad = collbad[0]
            
            collgood, collbad = make_lists()
        
# #             collgood1 = [['Brentwood', 6.9, 0.5, (205, 343)], ['London', 7.9, 0.3, (224, 280)], ['Southend-On-Sea', 7.9, 0.1, (180, 300)]]
# #             collbad2 = [['Manchester', 16.0, 0.0, (132, 0)], ['London', 9.1, 0.0, (150, 0)], ['Chelmsford', 5.1, 0.0, (200, 0)]]
# #             
# #             coll_proto1 = sorted(collgood1, key=lambda x: float(x[2]), reverse=True)
# #             coll_proto2 = sorted(coll_proto1, key=lambda x: float(x[1]), reverse=True)
            
# #             print("BWIMPH!", coll_proto2)
            
# #             if not "goody" in request.COOKIES:
# #                 goody = request.COOKIES.get("goody", collgood)
            goody = cookie_help2(request.COOKIES, "goody", collgood)
# #             if not "baddy" in request.COOKIES:
# #                 baddy = request.COOKIES.get("baddy", collbad)
            baddy = cookie_help2(request.COOKIES, "baddy", collbad)
            print("CRAM!!")

            #gus = plotto(collgood, collbad)
            gus = "Yes"
            print("GLOSS1 X", collgood[1][3][0])
            print("GLOSS1 Y", collgood[1][3][1])
            
#             response =  render(request, "plp/index.html", {"yee":paste, "poys":endo,
#                                                            "best":collgood, "worst":collbad, "gus":gus,
#                                                            "g1top": collgood[0][3][0], "g1left": collgood[0][3][1],
#                                                            "g2top": collgood[1][3][0], "g2left": collgood[1][3][1]})
#             if not "my_sesh" in request.COOKIES:
#                 response.set_cookie("my_sesh", make_id())
#                 response.set_cookie("goody", collgood)
#                 response.set_cookie("baddy", collbad)
        #elif "time_stamp" in request.COOKIES and right_now - the_time > timedelta(minutes=1):
        elif timefunc:
            nowy = datetime.now()
            time_stamp = cookie_help1(request.COOKIES, "time_stamp", nowy)
            collgood, collbad = make_lists()
            goody = cookie_help1(request.COOKIES, "goody", collgood)
            baddy = cookie_help1(request.COOKIES, "baddy", collbad)
            gus = "Yes"
            print("CLAIB REPEAT! bET IT'S gaRY nUMAN")
        
        
        else:
            collgood = ast.literal_eval(request.COOKIES["goody"])
            collbad = ast.literal_eval(request.COOKIES["baddy"])
            print("HEAR THAT SOUND!")
        response = render(request, "plp/index.html", {"best":collgood, "worst":collbad,
                            "g1top": int(collgood[0][3][0]), "g1left": int(collgood[0][3][1]),
                            "g2top": int(collgood[1][3][0]), "g2left": int(collgood[1][3][1]),
                            "g3top": int(collgood[2][3][0]), "g3left": int(collgood[2][3][1]),
                            "g4top": int(collgood[2][3][0]), "g4left": int(collgood[2][3][1]) + 100,
                            "b1top": int(collbad[0][3][0]), "b1left": int(collbad[0][3][1]),
                            "b2top": int(collbad[1][3][0]), "b2left": int(collbad[1][3][1]),
                            "b3top": int(collbad[2][3][0]), "b3left": int(collbad[2][3][1]),
                            "b4top": int(collbad[2][3][0]) - 100, "b4left": int(collbad[2][3][1])}
                          )
        if not "my_sesh" in request.COOKIES:
            response.set_cookie("my_sesh", make_id())
        response.set_cookie("goody", collgood)
        response.set_cookie("baddy", collbad)
        if timefunc:
            response.set_cookie("time_stamp", nowy)
    else:
        response =  render(request, "plp/index.html", {})

        
# # #     if not "blasty" in request.COOKIES:
# # #         blat = request.COOKIES.get("blasty", "TIBBY")
# # #     else:
# # #         blat = request.COOKIES["blasty"]
    
    #response =  render(request, "plp/index.html", {"yee":paste, "poys":endo})
# # #     if "searched" in request.COOKIES:
# # #         response.set_cookie("blasty", "TIBBY")
#     if not "my_sesh" in request.COOKIES:
#         response.set_cookie("my_sesh", make_id())
#         response.set_cookie("goody", collgood)
#         response.set_cookie("baddy", collbad)
    #if "time_stamp" in request.COOKIES:
        #print(type(request.COOKIES["time_stamp"]))
        #the_time = datetime.strptime(request.COOKIES["time_stamp"], "%Y-%m-%d %H:%M:%S.%f")
        #print(type(the_time))
    return response
