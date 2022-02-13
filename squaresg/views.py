from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.template import loader
from django.template.response import TemplateResponse
from django.views import generic
from django.utils import timezone
from django.db.models import Count
from django.views.generic.edit import FormMixin
from .forms import ChoiceForm, ScoreForm
from .service import make_list_for_view, randomise_squares, initial_cou
from .models import Choice, Question, Number, Exceppo, Scores, Times
from datetime import date, time, datetime, timedelta

# Create your views here.

class IndexuView(generic.ListView):
    template_name = "squaresg/indexu.html"
    context_object_name = "latest_question_list"
    
    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now()).exclude(choice__id=None).order_by("-pub_date")[:5]

def resetty(request):
    #Times.objects.all().delete()
    sesh = request.session._session_key
    if Number.objects.filter(sessiony=sesh).exists():
        Number.objects.filter(sessiony=sesh).delete()
    if Exceppo.objects.filter(sessiony=sesh).exists():
        Exceppo.objects.filter(sessiony=sesh).delete()
    if Times.objects.exists():
        timey = Times.objects.latest("id")
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
        if not Number.objects.filter(sessiony=self.request.session._session_key).exists():
            print("GLUT!", Number.objects.all())
            db = Number.objects.create(wardle = self.listy, sessiony = self.request.session._session_key)
            db.save()
        if not Exceppo.objects.filter(sessiony=self.request.session._session_key).exists():
            exp = Exceppo.objects.create(exceppy = self.exceppo, sessiony = self.request.session._session_key)
            print("BLEEK!")
            exp.save()
        
        return self.listy
    
    def get_form(self):
        return self.form
    
    def get_scores(self):
        return self.scores
    
    def get_duration(self):
        return self.times

def RandomSquaresView(request):
    gases = request.session._session_key
    
#     if not Number.objects.all().exists():
#         numbo = Number.objects.create(wardle = nine_squares_list, sessiony = gases)
#         numbo.save()

    print("I ALSO TRAVEL!", gases)
    SquaresInstance = SquaresView()

    
    print("KWARGS!!!!!!", Number.objects.all())

    #exceppo = Exceppo.objects.latest("id")
    exceppo = Exceppo.objects.filter(sessiony=gases).latest("id")
    form = SquaresInstance.get_form()
    scores = SquaresInstance.get_scores()
    clicked = request.GET.get("square_id")
    if not Times.objects.all().exists():
        db3 = Times.objects.create(start_time = datetime.now(), \
                                   finish_time = datetime.now(), sessiony = gases)
        db3.save()

    print("CLICKED: ", clicked)
    print("EXCEPPO NOW IT@S GOOD!:", exceppo)
    latest = Number.objects.filter(sessiony=gases).latest("id")
    listy2 = (str(latest).replace("'","").replace(",","").replace("[","").replace("]","")).split()
    print(type(listy2))
    print("LATEST, GREATEST?", listy2)
    nine_squares_list, cou, goes = randomise_squares(listy2, exceppo, clicked)
    db2 = Number.objects.create(wardle=nine_squares_list, sessiony = gases)
    db2.save()
    context = {"nine_squares_list":nine_squares_list, "cou":cou, "goes":goes,
               "exceppo":exceppo, "form":form, "scores":scores}
    url = "squaresg/squares.html"
    if request.method == "POST" and "squares_rand" in request.POST:
        return render(request, url, context)
    else:
        return render(request, url, context)

class DetailView(generic.DetailView):
    model = Question
    template_name = "squaresg/detail.html"
    
    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now()).exclude(choice__id=None)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["form"] = ChoiceForm()
        return context

class ResultsView(generic.DetailView):
    mode = Question
    template_name = "squaresg/results.html"
    
    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now()).exclude(choice__id=None)

def vote(request, question_id):
    form = ChoiceForm(initial=request.POST)
    question = get_object_or_404(Question, pk=question_id)
    if request.method=="POST" and "votey" in request.POST:
        print(request.POST)
        try:
            selected_choice = question.choice_set.get(pk=request.POST["choice"])
        except (KeyError, Choice.DoesNotExist):
            return render(request, "squaresg/detail.html", {"question":question,"error_message":"POY!!!","form":form})
        else:
            selected_choice.votes += 1
            selected_choice.save()
            return HttpResponseRedirect(reverse("squaresg:results", args=(question_id,)))
    else:
        return render(request, "squaresg/detail.html", {"question":question, "form":form})

def AddyChoice(request, question_id):
    questiony = get_object_or_404(Question, pk=question_id)
    if request.method == "POST" and "addey" in request.POST:
        form = ChoiceForm(request.POST)
        if form.is_valid():
            form.instance.question = questiony
            form.save()
            return HttpResponseRedirect(reverse("squaresg:detail", args=(question_id,)))
    else:
        form = ChoiceForm()
    return render(request, "squaresg/detail.html", {"form":form,"questiony":questiony})

def get_time():
    timey = Times.objects.latest("id")
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
    if request.method == "POST" and "saveIt" in request.POST:
        form = ScoreForm(request.POST)
        print(form)
        print("BLEAT???")
        if form.is_valid():
            print("PINT-SIZED PALS!!!")
            scores2 = (Number.objects.all().count())-1
            duration, seconds2, attempts = get_time()
            form.instance.score = int(scores2)
            form.instance.duration = str(duration)
            form.instance.all_seconds = int(seconds2)
            form.instance.attempts = int(attempts)
            print("I HAVE COVID!!", duration, seconds2)
            form.instance.duration = duration
            #form.instance.all_seconds = seconds2
            form.save()
            #Times.objects.all().delete()
            return HttpResponseRedirect(reverse("squaresg:resetto"))
    else:
        form = ScoreForm()
        print("YARROW?!?!?!?!?!?!?!?")
    print("BLAST LINE!!!!!")
    return render(request, "squaresg/squares.html", {"form":form})
    