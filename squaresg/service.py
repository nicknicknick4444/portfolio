from .logico.squares_logic import make_list, randomise2, make_cou
#from .models import Number, Exceppo, Times
import random

def make_list_for_view():
    listy, excep = make_list()
    return listy, excep

def make_id():
    session_id = random.randint(1000000000000000000000,9999999999999999999999)
    return str(session_id)+"GLAB"

def initial_cou(listy):
    return make_cou(listy)

def randomise_squares(squares, excep, clicked, reqc):
    listy, cou = randomise2(squares, excep, clicked, reqc)
    #if cou == "WIN":
        #goes = Number.objects.filter(sessiony=SESS).count()
    #goes = reqc.COOKIES["goesy"]
#     else:
#         goes = 0
    #return randomise2(squares, excep, clicked)
    return listy, cou

def datechange(the_date, functoken):
    return functoken(the_date, "%Y-%m-%d %H:%M:%S.%f")
