from .logico.squares_logic import make_list, randomise2, make_cou
#from .models import Number, Exceppo, Times
import random

def make_list_for_view():
    listy, excep = make_list()
    return listy, excep

def initial_cou(listy):
    return make_cou(listy)

def randomise_squares(squares, excep, clicked, reqc):
    listy, cou = randomise2(squares, excep, clicked, reqc)
    return listy, cou

def datechange(the_date, functoken):
    return functoken(the_date, "%Y-%m-%d %H:%M:%S.%f")

def cleanup2(reqc, reso):
    mainlist = ["namey", "boxo", "bisp", "chosen", "risp", "filtery", \
                "query_s", "query_u", "query_d", "design", "picked_colour", \
                "sum_list", "colours_list"]
    for i in mainlist:
        if i in reqc.COOKIES:
            reso.delete_cookie(i)
