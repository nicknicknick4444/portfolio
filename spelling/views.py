from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils import timezone
from datetime import timedelta
import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from .models import Tub, Admonish, TweetLists
from .logico.tweepy_practice import cookie_help, cookie_help_2, getty, send_tweet, api, make_id, get_answers, \
     lookup_answer, readie, make_lists, get_lists, page_turn
import json, datetime

gursp = ""
words = ""
#dicty2 = dicty2

# Create your views here.

def wordPick(request):
    chosen = request.POST.get("wordpicking")
    cookey = request.COOKIES.get("chosen", chosen)
    #bisp = cookie_help(request.COOKIES, "bisp", "Twiter Spelling Police")
    response = HttpResponseRedirect(reverse("spelling:index"))
    response.set_cookie("chosen", chosen)
    #response.set_cookie("bisp", bisp)
    print(chosen)
    return response

def searchy(request):
    # GET NOWY TO BE DATETIME FLOATING ACTUAL NOW, NOT FIXED FUCKING TIMEZONE.NOW()
    nowy = datetime.datetime.now(datetime.timezone.utc)
    #nowy = datetime.datetime.now()
    #bisp = bisp
    #bisp = cookie_help_2(request.COOKIES, "bisp", "Twitter Spelling Police", "Twitter Spelling Police")
    bisp = cookie_help(request.COOKIES, "bisp", "12345")
    
#     if not "seshn" in request.COOKIES:
#         seshn = request.COOKIES.get("seshn", make_id())
#     else:
#         seshn = request.COOKIES["seshn"]
    seshn = cookie_help(request.COOKIES, "seshn", make_id())
    #make_lists(seshn)
    #print("clurt")
    
    print("seshn WORKED:", seshn)
    checking = TweetLists.objects.filter(twe_seshn=seshn, twe_term="thye").values_list("twe_time")
    #checking = TweetLists.objects.filter(twe_seshn=seshn, twe_term="thye").values_list("twe_time")
    
    if "seshn" in request.COOKIES and not TweetLists.objects.filter(twe_seshn=seshn, twe_term="thye").exists():
        make_lists(seshn)
        print("GASSY2", checking)
#     elif "seshn" in request.COOKIES:
#         make_lists(seshn)
#         print("GURSE", checking)
    
        #checking = TweetLists.objects.filter(twe_seshn=seshn, twe_term="thye").values_list("twe_time")
#     else:
#         checking = TweetLists.objects.filter(twe_seshn=seshn, twe_term="thye").values_list("twe_time")
#         print("GASSY", checking)
#START HERE!!!!
    if checking.exists() and nowy - checking[0][0] > timedelta(minutes=20):
        TweetLists.objects.filter(twe_seshn=seshn).all().delete()
        print("PRYKE!")
        make_lists(seshn)
        print("GASSY", checking)
        #checking = TweetLists.objects.filter(twe_seshn=seshn, twe_term="thye").values_list("twe_time")
    
    
#     print("NOWY", type(nowy), nowy)
#     print("DB QUERY TIME", type(checking[0][0]), checking[0][0])
#     print("MAKE YOURSELF PLAST", type(checking[0][0] - nowy), nowy - checking[0][0], (nowy - checking[0][0]) < timedelta(minutes=15))
    
    whichp = "1 - 5"
    if "chosen" in request.COOKIES:
        wordu = request.COOKIES["chosen"]
    else:
        wordu = "blanku"
    
#     if "risp" in request.COOKIES:
#         rcooki = request.COOKIES["risp"]
#     else:
#         rcooki = request.COOKIES.get("risp", "START!")
    rcooki = cookie_help(request.COOKIES, "risp", "START!")
    
    
    print("rcooki WORKS???", rcooki)
    
    #wordu = "Gorpleborplehouse"

    #if "seshn" in request.COOKIES:
    if "chosen" in request.COOKIES and request.COOKIES["chosen"] != "blanku":
        #dicty2 = []
        dicty2 = get_lists(wordu, seshn)
#     else:
#          seshn = cookie_help(request.COOKIES, "seshn", make_id())
#          make_lists(seshn)
#          dicty2 = get_lists(wordu, seshn)
    else:
        dicty2 = [[[{"":"","":"","":"","":"","":""}],[]],[]]

    #print(goosey)
    #words = "HPointore Brothers!"
    if "answers" in request.COOKIES:
        cookie_words = request.COOKIES["answers"]
        vocab = readie(cookie_words)
    else:
        #vocab = readie(get_answers())
        vocab = get_answers()
        cookie_words = request.COOKIES.get("answers", vocab)
    print("POOSE", cookie_words)
    if wordu != "blanku":
        words = lookup_answer(vocab[wordu], wordu)
        #words = "DORP"
    else:
        words = ""
    print("GORP", vocab["thye"])
            
    clicked = request.GET.get("tweety_id")
    clicked2 = request.GET.get("tweety_text")
    clicked3 = request.GET.get("screen_name")
    #if request.COOKIES["risp"] == "THANK!":
    boxo = request.GET.get("boxo")
    marker = cookie_help(request.COOKIES, "boxo", boxo)
    print("Lengo", len(dicty2))
#     if not "namey" in request.COOKIES:
#         cookey = request.COOKIES.get("namey", clicked3)
#     else:
#         cookey = request.COOKIES["namey"]
        
    cookey = cookie_help(request.COOKIES, "namey", clicked3)
    print("cookey WORKED!!!!!!!", cookey)
        
    
#     if not "filtery" in request.COOKIES:
#         gus = request.COOKIES.get("filtery", str(1))
#     else:
#         gus = request.COOKIES["filtery"]
    
    
    gus = cookie_help(request.COOKIES, "filtery", str(1))
    print("gus WORKEDUH!!!!!!!", gus)
    
#     if int(gus) > 6:
#         gus = "6"
#         whichp = "26 - 30"
#     if int(gus) < 1:
#         gus = "1"
#         whichp = "1 - 5"
#     if gus == "1":
# 
#         dicty2 = dicty2[:5]
#         whichp = "1 - 5"
#     elif gus == "2":
#         dicty2 = dicty2[5:10]
#         whichp = "6 - 10"
#     elif gus == "3":
#         dicty2 = dicty2[10:15]
#         whichp = "11 - 15"
#     elif gus == "4":
# 
#         dicty2 = dicty2[15:20]
#         whichp = "16 - 20"
#     elif gus == "5":
#         dicty2 = dicty2[20:25]
#         whichp = "21 - 25"
#     elif gus == "6":
#         dicty2 = dicty2[25:30]
#         whichp = "26 - 30"
    dicty2, whichp = page_turn(gus, whichp, dicty2)
    #dicty2 = dicty2[1:3]
    
    
    conetext = {"tweets":dicty2, "gus":gus, "whichp":whichp, "wordu":wordu,
                "words":words, "clicked": clicked, "the_text":clicked2, "clicked3":clicked3, "boxo": boxo}
    response = render(request, "spelling/index.html", conetext)
    response.set_cookie("bisp", bisp)
    response.set_cookie("seshn", seshn)
    response.set_cookie("filtery", gus)
    response.set_cookie("chosen", wordu)
    response.set_cookie("risp", rcooki)
    response.set_cookie("namey", clicked3)
    response.set_cookie("answers", cookie_words)
    response.set_cookie("boxo", boxo)
    return response
    #return render(request, "spelling/index.html", conetext)

def filterup(request):
    response = HttpResponseRedirect(reverse("spelling:index"))
#     if not "filtery" in request.COOKIES:
#         numbu = request.COOKIES.get("filtery", str(1))
#     else:
#         numbu = int(request.COOKIES["filtery"])
    numbu = cookie_help_2(request.COOKIES, "filtery", str(1), int(request.COOKIES["filtery"]))
    response.set_cookie("filtery", str(numbu + 1))

    return response

def filterdown(request):
    response = HttpResponseRedirect(reverse("spelling:index"))
#     if not "filtery" in request.COOKIES:
#         numbu = request.COOKIES.get("filtery", str(1))
#     else:
#         numbu = int(request.COOKIES["filtery"])
    numbu = cookie_help_2(request.COOKIES, "filtery", str(1), int(request.COOKIES["filtery"]))
    response.set_cookie("filtery", str(numbu - 1))

    
    return response


def sure(request):
    global gursp
    global words
    #words = "Awesome!"
    #template = "spelling/to_send.html"
    template = "spelling/index.html"
    clicked = request.GET.get("tweety_id")
    #clicked3 = request.GET.get("screen_name")
    gursp = clicked
    wordu = request.COOKIES["chosen"]
    gus = request.COOKIES["filtery"]
    #risp = "Two bloo"
    print("RISP", risp)
    context = {"gus": gus, "wordu": wordu}
#     if not "sesho" in request.COOKIES:
#         cooki = request.COOKIES.get("sehso", make_id())
#     else:
#         cooki = request.COOKIES["sesho"]
    cooki = cookie_help(request.COOKIES, "sesho", make_id())

#     if not "namey" in request.COOKIES:
#         cookey = request.COOKIES.get("namey", clicked3)
#     else:
#         cookey = request.COOKIES["namey"]
    response = render(request, template, context)
    response.set_cookie("sesho", cooki)
    response.set_cookie("risp", "Two bloo")
#     response.set_cookie("namey", cookey)
    return response
    #return render(request, template, context)

def sendy(request):
    #word = "Bluncy!"
    cookie_words = request.COOKIES["answers"]
    vocab = readie(cookie_words)
    wordu = request.COOKIES["chosen"]
    word = lookup_answer(vocab[wordu], wordu)
    clicked = request.GET.get("tweety_id")
    #boxo = request.GET.get("boxo")
    
    #clicked3 = request.GET.get("screen_name")
    gursp = clicked
    print(gursp)
    #risp = "THIRD!"
    context = {"clicked":clicked}
    #api.update_status(status=word, in_reply_to_status_id=gursp, auto_populate_reply_metadata=True)
    send_tweet(word, gursp)
    response = HttpResponseRedirect(reverse("spelling:index"))
    #response = render(request, "spelling/index.html", context)
#     if not "done" in request.COOKIES:
#         cooko = request.COOKIES.get("done", make_id() + "BISP")
#     else:
#         cooko = request.COOKIES["done"]
    cooko = cookie_help(request.COOKIES, "done", clicked)
    #cooko = cookie_help(requescooko,)
    #return HttpResponseRedirect(reverse("spelling:index"))
    response.set_cookie("done", clicked)
    response.set_cookie("risp", "THANK!")
    #response.set_cookie("boxo", boxo)
    return response


def closey(request):
    response = HttpResponseRedirect(reverse("spelling:index"))
    response.set_cookie("risp", "STOP!")
    response.set_cookie("boxo", "FALSE")
    return response
