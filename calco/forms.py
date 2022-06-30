from django import forms
from .models import Colour

# class ColourChoose(forms.ModelForm):
#     colour_list = Colour.objects.values_list("colour_name", "colour_hex")
#     COLOR_CHOICES = [i for i in colour_list]
#     colour = forms.ChoiceField(choices = COLOUR_CHOICES)

