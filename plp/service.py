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

# badloc = [[1,51,290],[2,202,303],[3,253,340]]
# goodloc = [[1,363,162],[2,376,98],[3,285,19]]

def plotto(goodloc, badloc):
    #plt.rcParams["figure.figsize"] = [6.00,3.87]
    plt.rcParams["figure.autolayout"] = True
    im = plt.imread("./static/images/uk3.png")
    fig, ax = plt.subplots()
    #ax.xaxis.set_major_formatter(ticker.FormatStrFormatter("%1f"))
    im = ax.imshow(im, extent=[0, 387, 0, 600])
    #plt.figure()
# # #     for index, i in enumerate(goodloc):
# # #         x=i[3][0]
# # #         y=i[3][1]
# # #         plt.scatter(x,y,marker=".",color="#07e32b")
# # #         plt.text(x+4, y+1, str(index+1), fontsize=9)
# # #     
# # #     for index, i in enumerate(badloc):
# # #         #x = np.array(range(258))
# # #         x=i[3][0]
# # #         y=i[3][1]
# # #         #https://stackoverflow.com/questions/14432557/matplotlib-scatter-plot-with-different-text-at-each-data-point
# # #         
# # #         #plt.text(x, y, "YURKLE", fontdict=None, fontsize=12, ha="center", va="center")
# # #         #plt.scatter(x, y, ls=4, c="#ee0000")
# # #         plt.scatter(x,y, marker=".", color="#f70707")
# # #         plt.text(x+4, y+1, str(index+1), fontsize=9)
# # #         #ax.annotate(txt, x[1], y[1])
# # #         #ax.plot(x, x, ls="dotted", linewidth=2, color="#ee0000")

    plt.axis("off")
    plt.grid()
    major_ticks_top=np.linspace(0,400,9)
    #minor_ticks_top=np.linspace(0,400,9)
    major_ticks_bottom=np.linspace(0,600,13)
    ax.set_xticks(major_ticks_top)
    ax.set_yticks(major_ticks_bottom)
    ax.tick_params(axis="both", which="major", labelsize=8)
    fig.set_size_inches(2.58,4)
    fig.savefig("./static/images/uk3.png",bbinches="tight", dpi=113)
    print(fig)
    #print(picco)
# #     with io.BytesIO() as output:
# #         fig.set_size_inches(2.58,4).save(output, format="PNG")
# #         contents = output.getvalue()
# #     print(contents)
# # # #     picco_str = imagey(fig)
# # # #     print("GEEST", picco_str)
# # # #     db = SaveImage.objects.create(session_id = str(request.COOKIES["my_sesh"]), image = picco_str)
# # # #     db.save()
    
        #plt.show()
        #return ax.plot
def make_id():
    return random.randint(10000000000000000000, 99999999999999999999)
    
def imagey(my_image):
    with io.BytesIO() as output:
        image.save(output, format="PNG")
        contents = output.getvalue()

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
    

#placey = ["London","Manchester","Brentwood","Southend-On-Sea","Chelmsford"]

def make_lists():
    locdict = {"London":(100, 65), "Manchester":(90,150), "Brentwood":(205, 343),
           "Southend-On-Sea":(195,115), "Chelmsford":(210, 337)}
    
    
    
    
    
# # # # #     placey2 = {"Aberdeen": (189, 62),"Bath": (124, 339),"Brighton & Hove": (193, 378),"Chester": (135, 252),"Chelmsford": (210, 337),"Stortford": (199, 334),"Brentwood": (205, 343),"Billericay": (209, 343),"Southend-On-Sea": (),"Bristol": (),"Armagh": (),
# # # # #              "Bangor": (),"Belfast": (),"Birmingham": (),"Cambridge": (),"Cantebury": (),"Cardiff": (),"Carlisle": (),"Chichester": (),"Coventry": (),"Derby": (),"Derry": (),
# # # # #              "Dundee": (),"Durham": (),"Edinburgh": (),"Ely": (),"Exeter": (),"Glasgow": (),"Gloucester": (),"Hereford": (),"Inverness": (),"Kingston-Upon-Hull": (),
# # # # #              "Lancaster": (),"Leeds": (),"Leicester": (),"Lichfield": (),"Lincoln": (),"Lisburn": (),"Liverpool": (),"Manchester": (),"Newcastle-Upon-Tyne": (),
# # # # #              "Newport": (),"Newry": (),"Norwich": (),"Nottingham": (),"Oxford": (),"Perth": (),"Peterborough": (),"Plymouth": (),"Portsmouth": (),"Preston": (),"Ripon": (),
# # # # #              "St Albans": (),"St Asaph": (),"St Davids": (),"Salford": (),"Salisbury": (),"Sheffield": (),"Southampton": (),"Stirling": (),"Stoke-on-Trent": (),
# # # # #              "Sunderland": (),"Swansea": (),"Truro": (),"Wakefield": (),"Wells": (),"Wickford": (),"Winchester": (),"Wolverhampton": (),"Worcester": (),"York": ()}
# # # # #     
    
    
    #placey = ["London","Manchester","Brentwood","Southend-On-Sea","Chelmsford"]
    collection = []
    collgood = []
    collbad = []
    for p in locdict:
        litoure = []
        response = api_call(p)
        name = response.json()["location"]["name"]
        temp = response.json()["current"]["feelslike_c"]
        rainfall = response.json()["current"]["precip_mm"]
        coord = locdict[p]
        
        litoure.append(name)
        litoure.append(temp)
        litoure.append(rainfall)
        litoure.append(coord)
        collection.append(litoure)
        
    coll_proto1 = sorted(collection, key=lambda x: float(x[2]), reverse=True)
    #coll_proto1 = sorted(collection)
    print("CLUSE", collection)
    print("GRUSE", coll_proto1)
    coll_proto2 = sorted(coll_proto1, key=lambda x: float(x[1]), reverse=True)
    print("BRUSE", coll_proto2)
    collgood = [coll_proto2[:3]]
    collbad = [coll_proto2[:-4:-1]]
    ###collgood = [coll_proto1[:3]]
    ###collbad = [coll_proto1[-3:]]
    ##collgood = [i for i in reversed(collgood[0])]
    print("WOW!!", collgood)
    print("WORITA!", collbad)
    collgood = collgood[0]
    collbad = collbad[0]
    return collgood, collbad
