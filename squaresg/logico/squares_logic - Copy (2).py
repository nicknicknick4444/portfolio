import random
import json
#from ..models import Exceppo
from django.shortcuts import get_object_or_404
from django.utils import timezone
from datetime import date, time, datetime

# def make_rand_list_number():
#     if not Rand.exists():
        

def make_list():
    listy = ["square_"+ str(i) +".png" for i in range(1,10)]
    #rand_num = random.randint(1,10)
    ind = random.randint(0,8)
    #ind = 5-1
    excep = (listy.pop(ind))
#     if not data_token.objects.all().exists():
#         print("PEB!!")
#         excepsav = data_token.objects.create(exceppy = excep)
#         excepsav.save()
    #excep = data_token.objects.latest("id")
    listy.insert(ind, "token.png")
    print(listy[ind])
    print("TRUE JAWCY?", excep)
    print("GROOO!", listy)
#     listy2 = [i for i in listy]
#     random.shuffle(listy)
#     if listy == listy2:
#         return make_list(data_token)
#     else:
#         return listy, excep
    return listy, excep

def rand_choose(listy,listy2):
    q = random.choice(listy)
    if q in listy2:
        return rand_choose(listy, listy2)
    else:
        return q

# def randomise(listy):
#     #listy2 = []
#     #got = []
# #     while len(listy2) < len(listy):
# #         n = rand_choose(listy,listy2)
# #         listy2.append(n)
#     random.shuffle(listy)
    
    return listy

def make_cou(listy):
    if listy[0] == "token.png":
        cou = [listy[1], listy[3]]
    elif listy[1] == "token.png":
        cou = [listy[0], listy[2], listy[4]]
    elif listy[2] == "token.png":
        cou = [listy[1], listy[5]]
    elif listy[3] == "token.png":
        cou = [listy[0], listy[4], listy[6]]
    elif listy[4] == "token.png":
        cou = [listy[1], listy[3], listy[5], listy[7]]
    elif listy[5] == "token.png":
        cou = [listy[2], listy[4], listy[8]]
    elif listy[6] == "token.png":
        cou = [listy[3], listy[7]]
    elif listy[7] == "token.png":
        cou = [listy[4], listy[6], listy[8]]
    elif listy[8] == "token.png":
        cou = [listy[5], listy[7]]
    else:
        cou = []
    return cou

def win_test(listy, exceppo):
    listy2 = []
    listy2 = [i for i in listy]
    for index, i in enumerate(listy2):
        if listy2[index] == "token.png":
            listy2[index] = str(exceppo)
    if listy2 == ["square_1.png","square_2.png","square_3.png",
                 "square_4.png","square_5.png","square_6.png",
                 "square_7.png","square_8.png","square_9.png"]:
        print("Belinda Carlisle!")
        return True
    else:
        return False

def randomise2(listy, excep, clicked, data_token2):
    winning_test = False
    print("START OF RANDOMISE2!", listy)
    print("EXCEP!", excep)
    #clicked = "square_2.png"
    tokens = [clicked, "token.png"]
    tokens2 = tokens[::-1]
    print("SWITCH THIS:", tokens)
    print("WITH THIS:", tokens2)
    print(tokens2, "TOKENS2 REVERSED ETC")
    print("BEGIN:", listy)
    for index, n in enumerate(listy):
        #for index2, b in enumerate(tokens): 
        if n == tokens[0]:
            listy[index] = tokens2[0]
            print("FIRST SWAP:", listy)
            #listy[index] = "PUNCE!"
        elif n == tokens[1]:
            listy[index] = tokens2[1]
            print("SECOND SWAP", listy)

    cou = make_cou(listy)
    #where_now = 
    print("DONE!", listy)
    if win_test(listy, excep):
        listy = ["square_1.png","square_2.png","square_3.png",
                 "square_4.png","square_5.png","square_6.png",
                 "square_7.png","square_8.png","square_9.png"]
        time = data_token2.objects.latest("id")
        time.finish_time = datetime.now()
        time.save()
        cou = "WIN"
    #finish_time = time.finish_time
    return listy, cou

        
#listy = make_list()
#listy2 = randomise(listy)

# print(listy)
# print(listy2)