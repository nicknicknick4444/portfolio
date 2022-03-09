import random
import json
from django.shortcuts import get_object_or_404
from django.utils import timezone
from datetime import date, time, datetime

def make_list():
    listy = [str(i) for i in range(1,10)]
    ind = random.randint(0,8)
    excep = (listy.pop(ind))
    listy.insert(ind, "blank")
    # Easy mode activated!
    #random.shuffle(listy)
    return listy, excep

def make_cou(listy):
    if listy[0] == "blank":
        cou = [listy[1], listy[3]]
    elif listy[1] == "blank":
        cou = [listy[0], listy[2], listy[4]]
    elif listy[2] == "blank":
        cou = [listy[1], listy[5]]
    elif listy[3] == "blank":
        cou = [listy[0], listy[4], listy[6]]
    elif listy[4] == "blank":
        cou = [listy[1], listy[3], listy[5], listy[7]]
    elif listy[5] == "blank":
        cou = [listy[2], listy[4], listy[8]]
    elif listy[6] == "blank":
        cou = [listy[3], listy[7]]
    elif listy[7] == "blank":
        cou = [listy[4], listy[6], listy[8]]
    elif listy[8] == "blank":
        cou = [listy[5], listy[7]]
    else:
        cou = []
    return cou

def win_test(listy, exceppo):
    listy2 = []
    listy2 = [i for i in listy]
    for index, i in enumerate(listy2):
        if listy2[index] == "blank":
            listy2[index] = str(exceppo)
    if listy2 == ["1","2","3","4","5","6","7","8","9"]:
        return True
    else:
        return False

def randomise2(listy, excep, clicked, data_token2, gases):
    winning_test = False
    tokens = [clicked, "blank"]
    tokens2 = tokens[::-1]
    for index, n in enumerate(listy): 
        if n == tokens[0]:
            listy[index] = tokens2[0]
        # Next line is no longer elif, may have caused odd behaviour
        if n == tokens[1]:
            listy[index] = tokens2[1]

    cou = make_cou(listy)
    if win_test(listy, excep):
        listy = ["1","2","3","4","5","6","7","8","9"]
        time = data_token2.objects.filter(sessiony=gases).latest("id")
        time.finish_time = datetime.now()
        time.save()
        cou = "WIN"
    return listy, cou
