from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.template import loader
from django.template.response import TemplateResponse
from django.views import generic
from django.utils import timezone
from django.db.models import Count
from django.views.generic.edit import FormMixin
from .forms import ScoreForm
from .service import make_list_for_view, randomise_squares, \
     initial_cou, make_id, datechange
from .logico.squares_logic import cookie_help, cookie_help_2, randular
from .models import Squaresy, Scores
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
#     if "sesho" in request.COOKIES:
#         sesh = request.COOKIES["sesho"]
#     else:
#         sesh = "FIRST GLUPE"

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

def resetty2(request):
    response = HttpResponseRedirect(reverse("squaresg:squares"))
    request.session.set_test_cookie()
    you = request.COOKIES.get("sesho", str(make_id()))
    #sesh = you
    response.set_cookie("sesho", you)
    numboure, excepe = make_list_for_view()
    cou = initial_cou(numboure)
    squores = cookie_help(request, "squores", numboure)
    excepc = cookie_help(request, "excepor", excepe)
    print("excepc", excepc)
    print("eccepe", excepe)
    goesy = cookie_help(request, "goesy", 0)
    resety = cookie_help(request, "resety", 0)
    finishy_time = cookie_help(request, "finishy_time", 0)
    starty_time = cookie_help(request, "starty_time", "BEGIN!")
    cou2 = cookie_help(request, "cou", cou)
    print("cou", cou)
    
    response.set_cookie("squores", numboure)
    response.set_cookie("excepor", excepe)
    response.set_cookie("goesy", 0)
    response.set_cookie("resety", 0)
    response.set_cookie("starty_time", "BEGIN!")
    response.set_cookie("finishy_time", 0)
    response.set_cookie("cou", cou)
    #request.session["cached_yet"] = True
    
    return response

def SquaresView2(request):
    template = "squaresg/squares.html"
#     numboure = ast.literal_eval(request.COOKIES["squores"])
#     excepe = int(request.COOKIES["excepor"])
#     else:
#         pass
        #numboure, excepe = make_list_for_view()
        #numboure = ast.literal_eval(request.COOKIES["squores"])
        #excepe = int(request.COOKIES["excepor"])
    #if "cou" in request.COOKIES:
#     else:
#         pass
        #cou = initial_cou(numboure)
    form = ScoreForm
    scores = Scores.objects.all().order_by("score","all_seconds","attempts").values()[:10]
    if "squores" in request.COOKIES and "excepor" in request.COOKIES:
        numboure = ast.literal_eval(request.COOKIES["squores"])
        excepe = int(request.COOKIES["excepor"])
        cou = request.COOKIES["cou"]
        context = {"cou":cou, "exceppo":excepe, "form":form, "scores":scores, "nine_squares_list": numboure}
    else:
        context = {"scores":scores}
    return render(request, template, context)
    
    

def RandomSquaresView(request):
#     if "sesho" in request.COOKIES:
#         sesh = request.COOKIES["sesho"]
#     else:
#         sesh = "GLUPE"
    numbourey = ast.literal_eval(request.COOKIES["squores"])
    excepe = int(request.COOKIES["excepor"])
    turny = int(request.COOKIES["goesy"])
    if request.COOKIES["cou"] == "WIN":
        turny = turny
    else:
        turny += 1

    
    #print("MYSTIFY ME", numbourey[3], type(numbourey))
    
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
        response = render(request, url, context)
        response.set_cookie("squores", numbourey)
        response.set_cookies("goesy", turny)
        response.set_cookies("cou", cou)
        if request.COOKIES["starty_time"] == "BEGIN!":
            response.set_cookie("starty_time", datetime.now())
        response.set_cookie("finishy_time", datetime.now())
        return response
    else:
        response = render(request, url, context)
        response.set_cookie("squores", numbourey)
        response.set_cookie("goesy", turny)
        response.set_cookie("cou", cou)
        if request.COOKIES["starty_time"] == "BEGIN!":
            response.set_cookie("starty_time", datetime.now())
        response.set_cookie("finishy_time", datetime.now())
        return response

def get_time(request):
#     if "sesho" in request.COOKIES:
#         sesh = request.COOKIES["sesho"]
#     else:
#         sesh = "3rd GLUPE"
    tok = datetime.strptime
    dura = datechange(request.COOKIES["finishy_time"], tok) - \
           datechange(request.COOKIES["starty_time"], tok)
    
    print("NEEK!", dura, type(dura))
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
#     if "sesho" in request.COOKIES:
#         sesh = request.COOKIES["sesho"]
#     else:
#         sesh = "4th GLUPE"
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


def handler404(request, exception):
    #data = {}
    return render(request, "404.html", status=404)

def handler500(request):
    #data = {}
    return render(request, "500.html", status=500)

# 
# def custom_page_not_found(request):
#     return django.views.defaults.page_not_found(request, None)
# 
# def custom_server_error(request):
#     return django.views.defaults.server_error(request)

# 
# def error_403(request, exception):
#     data = {}
#     return render(request, "squaresg/403.html", data)
# 
# def error_400(request, exception):
#     data = {}
#     return render(request, "squaresg/400.html", data)

