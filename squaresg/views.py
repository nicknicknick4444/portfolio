from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.template import loader, RequestContext
from django.template.response import TemplateResponse
from django.views import generic
from django.utils import timezone
from django.db.models import Count
from django.views.generic.edit import FormMixin
from .forms import ScoreForm
from .service import make_list_for_view, randomise_squares, \
     initial_cou, datechange, cleanup2
from .logico.squares_logic import cookie_help, cookie_help_2, randular
from .models import Scores
from datetime import date, time, datetime, timedelta
import ast

# Create your views here.

class IndexView(generic.ListView):
    template_name = "squaresg/index.html"
    context_object_name = "a_queryset"
    
    def get_queryset(self):
        queryset = Scores.objects.none()
        return queryset

def resetty(request):
    resety = int(request.COOKIES["resety"])
    resety += 1
    numboure, excepe = make_list_for_view()
    cou = initial_cou(numboure)

    goesy = cookie_help(request, "goesy", 0)
    response = HttpResponseRedirect(reverse("squaresg:squares"))
    response.set_cookie("resety", resety)
    response.set_cookie("goesy", 0)
    response.set_cookie("squores", numboure)
    response.set_cookie("excepor", excepe)
    response.set_cookie("cou", cou)
    
    return response

def resetty3(request):
    response = HttpResponseRedirect(reverse("squaresg:squares"))
    if "squores" in request.COOKIES:
        numboure = request.COOKIES["squores"]
        excepe = request.COOKIES["excepor"]
        cou = request.COOKIES["cou"]
    else:
        numboure, excepe = make_list_for_view()
        cou = initial_cou(numboure)
    starty_time = cookie_help(request, "starty_time", "BEGIN!")
    finishy_time = cookie_help(request, "finishy_time", 0)
    goesy = cookie_help(request, "goesy", 0)
    resety = cookie_help(request, "resety", 0)
    
    cleanup2(request, response)
    response.set_cookie("squores", numboure)
    response.set_cookie("excepor", excepe)
    response.set_cookie("goesy", goesy)
    response.set_cookie("resety", resety)
    response.set_cookie("starty_time", starty_time)
    response.set_cookie("finishy_time", finishy_time)
    response.set_cookie("cou", cou)
    return response
    

def resetty2(request):
    response = HttpResponseRedirect(reverse("squaresg:squares"))
    request.session.set_test_cookie()
    numboure, excepe = make_list_for_view()
    cou = initial_cou(numboure)
    squores = cookie_help(request, "squores", numboure)
    goesy = cookie_help(request, "goesy", 0)
    resety = cookie_help(request, "resety", 0)
    finishy_time = cookie_help(request, "finishy_time", 0)
    starty_time = cookie_help(request, "starty_time", "BEGIN!")
    
    cleanup2(request, response)
    response.set_cookie("squores", numboure)
    response.set_cookie("excepor", excepe)
    response.set_cookie("goesy", 0)
    response.set_cookie("resety", 0)
    response.set_cookie("starty_time", "BEGIN!")
    response.set_cookie("finishy_time", 0)
    response.set_cookie("cou", cou)
    
    return response

def SquaresView2(request):
    template = "squaresg/squares.html"
    form = ScoreForm
    scores = Scores.objects.all().order_by("score","all_seconds","attempts").values()[:10]
    if "squores" in request.COOKIES and "excepor" in request.COOKIES and "cou" in request.COOKIES and "goesy" in request.COOKIES:
        numboure = ast.literal_eval(request.COOKIES["squores"])
        excepe = int(request.COOKIES["excepor"])
        cou = request.COOKIES["cou"]
        turny = request.COOKIES["goesy"]
        context = {"cou":cou, "exceppo":excepe, "form":form, "scores":scores, "nine_squares_list": numboure, "goes": turny}
    else:
        context = {"scores":scores}
    return render(request, template, context)
    

def RandomSquaresView(request):
    essence = ["squores", "cou", "goesy", "excepor", "starty_time", \
               "finishy_time", "resety"]
    for e in essence:
        if e not in request.COOKIES:
            return HttpResponseRedirect(reverse("squaresg:squares"))

    numbourey = ast.literal_eval(request.COOKIES["squores"])
    excepe = int(request.COOKIES["excepor"])
    turny = int(request.COOKIES["goesy"])
    if "cou" in request.COOKIES and request.COOKIES["cou"] == "WIN":
        turny = turny
    else:
        turny += 1
    
    form = ScoreForm
    
    scores = Scores.objects.all().order_by("score", "all_seconds", "attempts").values()[:10]
    clicked = request.GET.get("square_id")
    
    listy2 = numbourey
    nine_squares_list = numbourey
    numbourey, cou = randomise_squares(listy2, excepe, clicked, request)
    
    url = "squaresg/squares.html"

    if cou == "WIN":
        numbourey = [1,2,3,4,5,6,7,8,9]
    elif numbourey == [1,2,3,4,5,6,7,8,9]:
        cou = "WIN"

    context = {"nine_squares_list":numbourey, "cou":cou, "goes":turny,
           "exceppo":excepe, "form":form, "scores":scores}    
    if request.method == "POST" and "squares_rand" in request.POST:
        response = HttpResponseRequest(reverse("squaresg:squares"))

        response.set_cookie("squores", numbourey)
        response.set_cookies("goesy", turny)
        response.set_cookies("cou", cou)
        if request.COOKIES["starty_time"] == "BEGIN!":
            response.set_cookie("starty_time", datetime.now())
        response.set_cookie("finishy_time", datetime.now())
        return response
    else:
        response = HttpResponseRedirect(reverse("squaresg:squares"))
        response.set_cookie("squores", numbourey)
        response.set_cookie("goesy", turny)
        response.set_cookie("cou", cou)
        if request.COOKIES["starty_time"] == "BEGIN!":
            response.set_cookie("starty_time", datetime.now())
        response.set_cookie("finishy_time", datetime.now())
        return response

def get_time(request):
    tok = datetime.strptime
    dura = datechange(request.COOKIES["finishy_time"], tok) - \
           datechange(request.COOKIES["starty_time"], tok)
    
    days = dura.days
    hours = int(dura.seconds*3600)
    hours2 = round(int(dura.seconds/3600),0)
    seconds = int(round(dura.seconds%60,0))
    minutes = int(round(dura.seconds/60,0))
    seconds2 = dura.seconds
    attempts = request.COOKIES["resety"]
    if hours2 < 1:
        duration = str(hours2).zfill(2) + ":" + str(minutes).zfill(2) + ":" + str(seconds).zfill(2)
    elif days == 1:
        duration = str(days) + " day " + str(hours2).zfill(2) +":" + str(minutes).zfill(2) + ":" + str(seconds).zfill(2)
    elif hours2 >=1 and days < 1:
        duration = str(hours2).zfill(2) + ":" + str(minutes).zfill(2) + ":" + str(seconds).zfill(2)
    elif days > 1:
        duration = str(days) + " days " + str(hours2).zfill(2) + ":" + str(minutes).zfill(2) + ":" + str(seconds).zfill(2)
    elif days > 7:
        duration = str("FAILURE")
    
    return duration, seconds2, attempts

def Scoresy(request, *args, **kwargs):
    if request.method == "POST" and "saveIt" in request.POST:
        form = ScoreForm(request.POST)
        
        if form.is_valid():
            scores2 = int(request.COOKIES["goesy"])
            duration, seconds2, attempts = get_time(request)
            form.instance.score = int(scores2)
            form.instance.duration = str(duration)
            form.instance.all_seconds = int(seconds2)
            form.instance.attempts = int(attempts)
            form.instance.duration = duration
            form.save()
            return HttpResponseRedirect(reverse("squaresg:resetto2"))
    else:
        form = ScoreForm()
    return render(request, "squaresg/squares.html", {"form":form})

def ProjectsView(request):
    template="squaresg/projects.html"
    context = {}
    return render(request, template, context)

