from .service import api_call, plotto

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
import json


# Create your views here.

api_key = "b2bf55e4a6c24c55abe104821222603"

# https://www.weatherapi.com/

def subbo(request):
    response = HttpResponseRedirect(reverse("plp:index"))
    done = "done"
    if not "searched" in request.COOKIES:
        searching = request.COOKIES.get("searched", done)
    else:
        searching = request.COOKIES["searched"]
    response.set_cookie("searched", searching)
    return response
    

def poy(request):
    paste = "Yeeeee! Loveable drogue!"
    endo = []
    listy = [1,2,3,4,5,6,7,8,9,10]
    for i in listy:
        if i%2==0:
            endo.append("POY!")
    locdict = {"London":(300, 65), "Manchester":(200,300), "Brentwood":(75, 180), "Southend-On-Sea":(170,275), "Chelmsford":(200, 52)}
    placey = ["London","Manchester","Brentwood","Southend-On-Sea","Chelmsford"]
    #placey = ["London"]
    #placey = ['Wickford', 5.6, 0.0]
#     placey = ["Aberdeen","Bath","Brighton & Hove","Chester","Chelmsford","Stortford","Brentwood","Billericay","Southend-On-Sea","Bristol","Armagh",
#              "Bangor","Belfast","Birmingham","Cambridge","Cantebury","Cardiff","Carlisle","Chichester","Coventry","Derby","Derry",
#              "Dundee","Durham","Edinburgh","Ely","Exeter","Glasgow","Gloucester","Hereford","Inverness","Kingston-Upon-Hull",
#              "Lancaster","Leeds","Leicester","Lichfield","Lincoln","Lisburn","Liverpool","Manchester","Newcastle-Upon-Tyne",
#              "Newport","Newry","Norwich","Nottingham","Oxford","Perth","Peterborough","Plymouth","Portsmouth","Preston","Ripon",
#              "St Albans","St Asaph","St Davids","Salford","Salisbury","Sheffield","Southampton","Stirling","Stoke-on-Trent",
#              "Sunderland","Swansea","Truro","Wakefield","Wells","Wickford","Winchester","Wolverhampton","Worcester","York"]
    collection = []
#     collgood = []
#     collbad = []
    #response = requests.get("http://api.weatherapi.com/v1/current.json?key=b2bf55e4a6c24c55abe104821222603&q={}".format(placey))
    
    for p in placey:
        litoure = []
        response = api_call(p)
        #response = requests.get("http://api.weatherapi.com/v1/current.json?key=b2bf55e4a6c24c55abe104821222603&q={}".format(p))
        #print(response.json())
        name = response.json()["location"]["name"]
        temp = response.json()["current"]["feelslike_c"]
        rainfall = response.json()["current"]["precip_mm"]
        coord = locdict[p]
        #litoure = [location, temp, rainfall]
        
        litoure.append(name)
        litoure.append(temp)
        litoure.append(rainfall)
        litoure.append(coord)
        collection.append(litoure)
        #print(collection)
        
# # # #         collgood.append(litoure)
# # # #         collbad.append(litoure)
    coll_proto1 = sorted(collection, key=lambda x: int(x[1]))
    coll_proto2 = sorted(coll_proto1, key=lambda x: int(x[2]))
    collgood = [coll_proto2[:3]]
    collbad = [coll_proto2[-3:]]
    collgood = collgood[0]
    collbad = [i for i in reversed(collbad[0])]
    ###collgood = [['Brentwood', 0.9, 0.0, (75, 180)], ['London', 7.9, 0.0, (300, 65)], ['Southend-On-Sea', 7.4, 0.0, (170, 275)]]
    ###collbad = [['Manchester', 16.0, 0.0, (200, 300)], ['London', 9.1, 0.0, (300, 65)], ['Chelmsford', 5.1, 0.0, (200, 52)]]
    ###print("GOOD", collgood)
    ###print("BAD", collbad)
    #print(response.json()["current"]["wind_mph"])
    gus = plotto(collgood, collbad)
    
    return render(request, "plp/index.html", {"yee":paste, "poys":endo,
                                              "best":collgood, "worst":collbad,  "gus":gus})

