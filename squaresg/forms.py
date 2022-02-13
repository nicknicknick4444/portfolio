from django import forms
from .models import Choice, Scores

class ChoiceForm(forms.ModelForm):

    class Meta:
        model = Choice
        choice_text = "Geeseys"
        votes = 0
        fields = ["choice_text",]
        labels = {"choice_text":"New Choice"}

class ScoreForm(forms.ModelForm):
    
    class Meta:
        model = Scores
        namey = "Type Your Name"
        #score = 0
        fields = ["namey",]
        labels = {"namey":"Type Your Name"}
