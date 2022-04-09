import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import requests
import random
import io

#from .models import SaveQuery
from io import BytesIO

def api_call(q):
    return requests.get("http://api.weatherapi.com/v1/current.json?key=b2bf55e4a6c24c55abe104821222603&q={}".format(q))


def make_id():
    return random.randint(10000000000000000000, 99999999999999999999)

def cookie_help1(reqc, name, func):
    if name not in reqc:
        var = reqc.get(name, func)
    else:
        var = reqc[name]
    return var

def cookie_help2(reqc, name, func):
    if name not in reqc:
        var = reqc.get(name, func)
    return var

def time_check(a, reqc, b, c, d):
    if a in reqc and b - c > d:
        return True

def make_lists():
    placey2 = {"Aberdeen": (188, 63),"Bath": (123, 340),"Brighton & Hove": (192, 379),"Chester": (136, 255),"Chelmsford": (209, 338),"Stortford": (198, 335),"Brentwood": (204, 345),"Billericay": (208, 345),"Southend-On-Sea": (221, 348),"Bristol": (118, 337),"Armagh": (37, 179),
             "Bangor": (96, 248),"Belfast": (59, 172),"Birmingham": (149, 284),"Cambridge": (203, 315),"Cantebury": (227, 364),"Cardiff": (104, 336),"Carlisle": (144, 177),"Chichester": (174,375),"Coventry": (148, 291),"Derby": (162, 278),"Derry": (27, 147),
             "Dundee": (155, 106),"Durham": (169, 185),"Edinburgh": (141, 125),"Ely": (210, 310),"Exeter": (87, 366),"Glasgow": (110, 121),"Gloucester": (126, 328),"Hereford": (119, 311),"Inverness": (130, 48),"Kingston-Upon-Hull": (206, 244),
             "Lancaster": (140, 213),"Leeds": (165, 228),"Leicester": (169, 289),"Lichfield": (160, 286),"Lincoln": (192, 270),"Lisburn": (54, 177),"Liverpool": (129, 244),"Manchester": (153, 245),"Newcastle-Upon-Tyne": (172, 180),
             "Newport": (109, 331),"Newry": (44, 191),"Norwich": (241, 305),"Nottingham": (168, 283),"Oxford": (160, 336),"Perth": (140, 107),"Peterborough": (194, 303),"Plymouth": (63, 380),"Portsmouth": (170, 379),"Preston": (138, 229),"Ripon": (167, 212),
             "St Albans": (189, 340),"St Asaph": (114, 250),"St Davids": (51, 300),"Salford": (151, 243),"Salisbury": (142, 359),"Sheffield": (170, 246),"Southampton": (152, 368),"Stirling": (125, 112),"Stoke-on-Trent": (151, 270),
             "Sunderland": (178, 187),"Swansea": (85, 321),"Truro": (42, 376),"Wakefield": (166, 232),"Wells": (118, 345),"Wickford": (210, 344),"Winchester": (156, 361),"Wolverhampton": (145, 280),"Worcester": (143, 302),"York": (184, 226)}
    
    collection = []
    collgood = []
    collbad = []
    for p in placey2:
        litoure = []
        response = api_call(p)
        name = response.json()["location"]["name"]
        temp = response.json()["current"]["feelslike_c"]
        rainfall = response.json()["current"]["precip_mm"]
        coord = placey2[p]
        
        litoure.append(name)
        litoure.append(temp)
        litoure.append(rainfall)
        litoure.append(coord)
        collection.append(litoure)
        
    coll_proto1 = sorted(collection, key=lambda x: float(x[1]), reverse=True)
    coll_proto2 = sorted(coll_proto1, key=lambda x: float(x[2]))
    collgood = [coll_proto2[:5]]
    collbad = [coll_proto2[:-6:-1]]
    collgood = collgood[0]
    collbad = collbad[0]
    return collgood, collbad

def cleanup_cookies(reqc, resp):
    mainlist = ["sesho", "cou", "startytime", "finishy_time", "excepor", "resety", "squores", "goesy",
                "namey", "boxo", "bisp", "chosen", "risp", "filtery"]
    for i in mainlist:
        if i in reqc.COOKIES:
            resp.delete_cookie(i)
