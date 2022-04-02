from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils import timezone
from datetime import timedelta
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from .models import Tub, Admonish, TweetLists
from .logico.tweepy_practice2 import cookie_help, cookie_help_2, getty, send_tweet, api, make_id, get_answers, \
     lookup_answer, readie, make_lists, get_lists, page_turn
from .service import cleanup
import json, datetime


# Create your views here.

def wordPick(request):
    chosen = request.POST.get("wordpicking")
    cookey = request.COOKIES.get("chosen", chosen)
    response = HttpResponseRedirect(reverse("spelling:index"))
    response.set_cookie("chosen", chosen)
    return response

def searchy(request):
    nowy = datetime.datetime.now(datetime.timezone.utc)
    #bisp = cookie_help(request.COOKIES, "bisp", "12345")
    
    if not "seshn" in request.COOKIES:
        seshn = cookie_help(request.COOKIES, "seshn", make_id())
    else:
        seshn = request.COOKIES["seshn"]
    
    checking = TweetLists.objects.filter(twe_seshn=seshn, twe_term="thye").values_list("twe_time")
    
    if "seshn" in request.COOKIES and not TweetLists.objects.filter(twe_seshn=seshn, twe_term="thye").exists():
        make_lists(seshn)
    
    if checking.exists() and nowy - checking[0][0] > timedelta(minutes=20):
        TweetLists.objects.filter(twe_seshn=seshn).all().delete()
        make_lists(seshn)
        
    whichp = "1 - 5"
    if "chosen" in request.COOKIES:
        wordu = request.COOKIES["chosen"]
    else:
        wordu = "blanku"
    rcooki = cookie_help(request.COOKIES, "risp", "START!")
    
    if "chosen" in request.COOKIES and request.COOKIES["chosen"] != "blanku":
        dicty2 = get_lists(wordu, seshn)
    else:
        dicty2 = [[[{"":"","":"","":"","":"","":""}],[]],[]]
    
    if "answers" in request.COOKIES:
        cookie_words = request.COOKIES["answers"]
        vocab = readie(cookie_words)
    else:
        vocab = get_answers()
        cookie_words = request.COOKIES.get("answers", vocab)
                
    clicked = request.GET.get("tweety_id")
    
    if wordu != "blanku":
        words = lookup_answer(vocab[wordu], wordu)
        get_text = "".join([i["tweet_text"] for i in dicty2 if i["tweet_id"] == str(clicked)])
    else:
        words = ""
        get_text = ""
    
    clicked3 = request.GET.get("screen_name")

    boxo = request.GET.get("boxo")
    marker = cookie_help(request.COOKIES, "boxo", boxo)
    cookey = cookie_help(request.COOKIES, "namey", clicked3)
    gus = cookie_help(request.COOKIES, "filtery", str(1))
    dicty2, whichp = page_turn(gus, whichp, dicty2)
    
    
    conetext = {"tweets":dicty2, "gus":gus, "whichp":whichp, "wordu":wordu,
                "words":words, "clicked": clicked, "the_text":get_text, "clicked3":clicked3, "boxo": boxo}
    response = render(request, "spelling/index.html", conetext)
    cleanup(request, response)
    #response.set_cookie("bisp", bisp)
    response.set_cookie("seshn", seshn)
    response.set_cookie("filtery", gus)
    response.set_cookie("chosen", wordu)
    response.set_cookie("risp", rcooki)
    response.set_cookie("namey", clicked3)
    response.set_cookie("answers", cookie_words)
    response.set_cookie("boxo", boxo)
    return response

def filterup(request):
    response = HttpResponseRedirect(reverse("spelling:index"))
    numbu = cookie_help_2(request.COOKIES, "filtery", str(1), int(request.COOKIES["filtery"]))
    response.set_cookie("filtery", str(numbu + 1))
    return response

def filterdown(request):
    response = HttpResponseRedirect(reverse("spelling:index"))
    numbu = cookie_help_2(request.COOKIES, "filtery", str(1), int(request.COOKIES["filtery"]))
    response.set_cookie("filtery", str(numbu - 1))
    return response


def sure(request):
    template = "spelling/index.html"
    clicked = request.GET.get("tweety_id")

    gursp = clicked
    wordu = request.COOKIES["chosen"]
    gus = request.COOKIES["filtery"]
    context = {"gus": gus, "wordu": wordu}

    cooki = cookie_help(request.COOKIES, "sesho", make_id())

    response = render(request, template, context)
    response.set_cookie("sesho", cooki)
    response.set_cookie("risp", "Two bloo")
    return response

def sendy(request):
    cookie_words = request.COOKIES["answers"]
    vocab = readie(cookie_words)
    wordu = request.COOKIES["chosen"]
    word = lookup_answer(vocab[wordu], wordu)
    clicked = request.GET.get("tweety_id")
    gursp = clicked
    context = {"clicked":clicked}
    send_tweet(word, gursp)
    response = HttpResponseRedirect(reverse("spelling:index"))

    cooko = cookie_help(request.COOKIES, "done", clicked)

    response.set_cookie("done", clicked)
    response.set_cookie("risp", "THANK!")

    return response


def closey(request):
    response = HttpResponseRedirect(reverse("spelling:index"))
    response.set_cookie("risp", "STOP!")
    response.set_cookie("boxo", "FALSE")
    return response
