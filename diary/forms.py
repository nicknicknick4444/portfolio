from django import forms
from django.forms import Form, ModelForm, DateField, ModelMultipleChoiceField
from django.contrib.auth.models import User
#from django.forms.extras.widgets import SelectDateWidget
from .models import Entry
from functools import partial
#from django.forms.widgets import DateInput

# class DateInput(forms.DateInput):
#     input_type="date"


# YEAR_CHOICES = ["2022","2023","2024"]
# MONTH_CHOICES = ["04", "05"]
# DAY_CHOICES = ["01", "02"]

class UserChoiceField(ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        return obj.first_name
    
#DateInput = partial(forms.DateInput, {"class":"datepicker"})

que = User.objects.values_list("first_name", flat=True)
que2 = User.objects.values_list("first_name", "last_name")
#que2 = [((i for i in que) i in que) for i in que]
print([(i,i) for i in que])
print([i for i in que2])
#print(que2)

class NewEntryForm(ModelForm):
#     def __init__(self, *args, **kwargs):
#         super(NewEntryForm, self).__init__(*args, **kwargs)
#         self.fields["user"] = forms.ModelMultipleChoiceField(queryset=User.objects.filter(username__startswith="M"))
    
    user = forms.ChoiceField(choices=que)
    #user = UserChoiceField
    #forms.ChoiceField.input_type="select"
    #forms.ChoiceField( choices=tuple_of_tuples)
    #user = forms.CharField(widget=forms.Textarea())
    
    #queryset = User.objects.filter(username__startswith="M")
    #print(queryset)
#     def get_form(self, request, obj, **kwargs):
#         form = super(NewEntryForm, self).get_form(request, obj, **kwargs)
#         form.base_fields["user"] = forms.ModelChoiceField(queryset)
#         print("PASTE!")
#         return form
    
    #form["user"] = forms.ModelChoiceField(queryset)
    #print(user)
    forms.DateInput.input_type="date"
    
    print("PAPER!", User.objects.filter(first_name__startswith="M"))
    #print("PAPYRUS!", User.objects.all(), to_field_name="first_name")
#     def __init__(self, *args, **kwargs):
#         super(NewEntryForm, self).__init__(*args, **kwargs)
#         self.fields["user"].initial = self.instance.user.first_name
#         
#     def save(self, *args, **kwargs):
#         super(NewEntryForm, self).save(*args, **kwargs)
#         self.instance.user.first_name = self.cleaned_data.get("first_name")
#         self.instance.user.save()
    
    class Meta:
        model = Entry
        #borce = MyModelChoiceField(queryset=Entry.objects.all())
        fields = "__all__"
        exclude = ("by", "date_written")
    
#        def __init__(self, *args, **kwargs):
#             super(NewEntryForm, self).__init__(*args, **kwargs)
#             self.fields["user"].queryset = User.objects.all()
#             self.fields["user"].label_from_instance = lambda obj: obj.first_name
        



# class SearchForm(forms.Form):
#     class Meta:
#         termy = forms.CharField(max_length=1000, default="")
    
    