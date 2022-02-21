from .logico.squares_logic import make_list, randomise2, make_cou
from .models import Number, Exceppo, Times

def make_list_for_view():
    listy, excep = make_list()
    return listy, excep


def initial_cou(listy):
    return make_cou(listy)

def randomise_squares(squares, excep, clicked, SESS):
    listy, cou = randomise2(squares, excep, clicked, Times, SESS)
    if cou == "WIN":
        goes = Number.objects.filter(sessiony=SESS).count()
    else:
        goes = 0
    #return randomise2(squares, excep, clicked)
    return listy, cou, goes

