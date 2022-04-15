from django import forms
from django.forms import Form, ModelForm, DateField
#from django.forms.extras.widgets import SelectDateWidget
from .models import Entry
from functools import partial
#from django.forms.widgets import DateInput

# class DateInput(forms.DateInput):
#     input_type="date"


YEAR_CHOICES = ["2022","2023","2024"]
MONTH_CHOICES = ["04", "05"]
DAY_CHOICES = ["01", "02"]

DateInput = partial(forms.DateInput, {"class":"datepicker"})

class NewEntryForm(ModelForm):
    forms.DateInput.input_type="date"
    class Meta:
        model = Entry

        fields = "__all__"
        exclude = ("by", "date_written")

# class SearchForm(forms.Form):
#     class Meta:
#         termy = forms.CharField(max_length=1000, default="")
    
    