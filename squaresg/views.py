from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.sessions.backends.db import SessionStore
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.template import loader
from django.template.response import TemplateResponse
from django.views import generic
from django.utils import timezone
from django.db.models import Count
from django.views.generic.edit import FormMixin
from .forms import ScoreForm
from .service import make_list_for_view, randomise_squares, initial_cou#, make_id
from .models import Number, Exceppo, Scores, Times
from datetime import date, time, datetime, timedelta
import random

sstore = SessionStore()
sstore.create()
seshy = sstore.session_key


# Create your views here.

class IndexView(generic.ListView):
    template_name = "squaresg/index.html"
    context_object_name = "a_queryset"
    
    def get_queryset(self):
#         return Question.objects.filter(pub_date__lte=timezone.now()).exclude(choice__id=None).order_by("-pub_date")[:5]
        queryset = Number.objects.none()
        return queryset

def resetty(request):
    sesh = seshy
    if Number.objects.filter(sessiony=sesh).exists():
        Number.objects.filter(sessiony=sesh).delete()
    if Exceppo.objects.filter(sessiony=sesh).exists():
        Exceppo.objects.filter(sessiony=sesh).delete()
    if Times.objects.filter(sessiony=sesh).exists():
        timey = Times.objects.filter(sessiony=sesh).latest("id")
        att = timey.attempts
        att += 1
        timey.attempts = att
        print("ATTEMPTS: ", timey.attempts)
        timey
        timey.save()
    return HttpResponseRedirect(reverse("squaresg:squares"))

def resetty2(request):
    sesh = request.session._session_key
    print("I TRAVEL",sesh)
    Number.objects.filter(sessiony=sesh).delete()
    Exceppo.objects.filter(sessiony=sesh).delete()
    Times.objects.filter(sessiony=sesh).delete()
    return HttpResponseRedirect(reverse("squaresg:squares"))

class SquaresView(generic.ListView):
    def __init__(self):
        self.template_name = "squaresg/squares.html"
        self.context_object_name = "nine_squares_list"
        self.listy = ""
        self.exceppo = ""
        self.listy, self.exceppo = make_list_for_view()
        print("PLAG!")

        self.cou = initial_cou(self.listy)
        self.form = ScoreForm
        self.scores = Scores.objects.all().order_by("score", "all_seconds", "attempts").values()[:10]
        self.extra_context = {"cou": self.cou, "exceppo": self.exceppo,
                              "form": self.form, "scores": self.scores,}
        
    def get_queryset(self):        
        #if not Number.objects.filter(sessiony = self.request.session._session_key).exists():
        if not Number.objects.filter(sessiony = seshy).exists():
            #print("GLUT!", Number.objects.all())
            print("TRAB!", seshy)
            #print("BRIXS", self.request.session._session_key)
            #db = Number.objects.create(wardle = self.listy, sessiony = self.request.session._session_key)
            db = Number.objects.create(wardle = self.listy, sessiony = seshy)
            db.save()
        else:
            #Number.objects.filter(sessiony = self.request.session._session_key).all().delete()
            Number.objects.filter(sessiony = seshy).all().delete()
            #db = Number.objects.create(wardle = self.listy, sessiony = self.request.session._session_key)
            db = Number.objects.create(wardle = self.listy, sessiony = seshy)
            db.save()
        #if not Exceppo.objects.filter(sessiony = self.request.session._session_key).exists():
        if not Exceppo.objects.filter(sessiony = seshy).exists():
            #exp = Exceppo.objects.create(exceppy = self.exceppo, sessiony = self.request.session._session_key)
            exp = Exceppo.objects.create(exceppy = self.exceppo, sessiony = seshy)
            print("BLEEK!", seshy)
            exp.save()
        else:
            #Exceppo.objects.filter(sessiony = self.request.session._session_key).all().delete()
            Exceppo.objects.filter(sessiony = seshy).all().delete()
            #exp = Exceppo.objects.create(exceppy = self.exceppo, sessiony = self.request.session._session_key)
            exp = Exceppo.objects.create(exceppy = self.exceppo, sessiony = seshy)
            print("POASTY!", seshy)
            exp.save()
        
        return self.listy
    
    def get_form(self):
        return self.form
    
    def get_scores(self):
        return self.scores
    
    def get_duration(self):
        return self.times

def RandomSquaresView(request):
    #sesh = request.session._session_key
    sesh = seshy
    SquaresInstance = SquaresView()
    print("I ALSO TRAVEL!", sesh)
    #exceppo = Exceppo.objects.latest("id")
    exceppo = Exceppo.objects.filter(sessiony=sesh).latest("id")
    form = SquaresInstance.get_form()
    scores = SquaresInstance.get_scores()
    clicked = request.GET.get("square_id")
    if not Times.objects.filter(sessiony=sesh).exists():
        db3 = Times.objects.create(start_time = datetime.now(), \
                                   finish_time = datetime.now(), sessiony = sesh)
        db3.save()

    print("CLICKED: ", clicked)
    print("EXCEPPO NOW IT@S GOOD!:", exceppo)
    latest = Number.objects.filter(sessiony=sesh).latest("id")
    listy2 = (str(latest).replace("'","").replace(",","").replace("[","").replace("]","")).split()
    print(type(listy2))
    print("LATEST, GREATEST?", listy2)
    nine_squares_list, cou, goes = randomise_squares(listy2, exceppo, clicked, sesh)
    #nine_squares_list2 = [" " for i in nine_squares_list if i == "&nbsp;"]
    db2 = Number.objects.create(wardle=nine_squares_list, sessiony = sesh)
    db2.save()
    context = {"nine_squares_list":nine_squares_list, "cou":cou, "goes":goes,
               "exceppo":exceppo, "form":form, "scores":scores}
    print("COU?", cou)
    
    
    url = "squaresg/squares.html"

    if cou == "WIN":
        Number.objects.filter(sessiony=sesh).latest("id").delete()
    if request.method == "POST" and "squares_rand" in request.POST:
        return render(request, url, context)
    else:
        return render(request, url, context)

def get_time(request):
    #sesh = request.session._session_key
    sesh = seshy
    timey = Times.objects.filter(sessiony=sesh).latest("id")
    dura = timey.finish_time - timey.start_time
    days = dura.days
    hours = int(dura.seconds*3600)
    hours2 = round(int(dura.seconds/3600),0)
    seconds = int(round(dura.seconds%60,0))
    minutes = int(round(dura.seconds/60,0))
    seconds2 = dura.seconds
    attempts = timey.attempts
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
    print("Elapsed!", duration)
    
    return duration, seconds2, attempts

def Scoresy(request, *args, **kwargs):
    #sesh = request.session._session_key
    sesh = seshy
    if request.method == "POST" and "saveIt" in request.POST:
        form = ScoreForm(request.POST)
        print(form)
        print("BLEAT???")
        if form.is_valid():
            print("PINT-SIZED PALS!!!")
            scores2 = (Number.objects.filter(sessiony=sesh).all().count())
            duration, seconds2, attempts = get_time(request)
            form.instance.score = int(scores2)
            form.instance.duration = str(duration)
            form.instance.all_seconds = int(seconds2)
            form.instance.attempts = int(attempts)
            print("I HAVE COVID!!", duration, seconds2)
            form.instance.duration = duration
            #form.instance.all_seconds = seconds2
            form.save()
            Times.objects.filter(sessiony=sesh).all().delete()
            return HttpResponseRedirect(reverse("squaresg:resetto"))
    else:
        form = ScoreForm()
        print("YARROW?!?!?!?!?!?!?!?")
    print("BLAST LINE!!!!!")
    return render(request, "squaresg/squares.html", {"form":form})
    