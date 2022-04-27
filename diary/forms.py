from django import forms
from django.forms import Form, ModelForm, DateField, ModelMultipleChoiceField, \
     PasswordInput, EmailInput
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
#from django.forms.extras.widgets import SelectDateWidget
from .models import Entry, SendTime
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

queryo = User.objects.values_list("first_name", flat=True)
queryo2 = User.objects.values_list("first_name", "last_name")
#que2 = [((i for i in que) i in que) for i in que]
print([(i,i) for i in queryo])
print([i for i in queryo2])
#print(que2)

class NewEntryForm(ModelForm):
#     def __init__(self, *args, **kwargs):
#         super(NewEntryForm, self).__init__(*args, **kwargs)
#         self.fields["user"] = forms.ModelMultipleChoiceField(queryset=User.objects.filter(username__startswith="M"))
    
    user = forms.ChoiceField(choices=queryo)
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
        exclude = ("by", "mod_by", "date_written")
    
#        def __init__(self, *args, **kwargs):
#             super(NewEntryForm, self).__init__(*args, **kwargs)
#             self.fields["user"].queryset = User.objects.all()
#             self.fields["user"].label_from_instance = lambda obj: obj.first_name
        
class CreateUserForm(ModelForm):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=PasswordInput)
    email = forms.CharField(widget=EmailInput)
    first_name = forms.CharField(max_length=100, label="Name")
    last_name_ = forms.CharField(max_length=100, label="Initial")
    
    class Meta:
        model = User
        fields = ["username", "password", "email", "first_name", "last_name"]

# class MyUserChangeForm(UserChangeForm):
#     def __init__(aelf, *args, **kwargs):
#         super(MyUserChangeForm, self).__init__(*args, **kwargs)
#     
#         self.fields["first_name"].required = True

class SetTimeForm(forms.Form):
    HOUR_OPTIONS = [("01", "1am"), ("02", "2am"), ("03", "3am"), ("04", "4am"), ("05", "5am"), ("06", "6am"),
                    ("07", "7am"), ("08", "8am"), ("09", "9am"), ("10", "10am"), ("11", "11am"), ("12", "12am"),
                    ("13", "1pm"), ("14", "2pm"), ("15", "3pm"), ("16", "4pm"), ("17", "5pm"), ("18", "6pm"),
                    ("19", "7pm"), ("20", "8pm"), ("21", "9pm"), ("22", "10pm"), ("23", "11pm"), ("00", "12pm")]
    MINUTE_OPTIONS = [("00", "00"), ("15", "15"), ("30", "30"), ("45", "45")]
    #hour = forms.CharField(label="Hour", widget=forms.Select(choices=HOUR_OPTIONS))
    #minute = forms.CharField(label="Minute", widget=forms.Select(choices=MINUTE_OPTIONS))
    hour = forms.ChoiceField(choices=HOUR_OPTIONS)
    minute = forms.ChoiceField(choices=MINUTE_OPTIONS, initial="00")
    #proto_send_time = "".join((send_time, ":", minute))
    #print(proto_send_time)
    #send_time = 
    
    class Meta:
        #model = SendTime
        fields = ["hour", "minute"]

# class SearchForm(forms.Form):
#     class Meta:
#         termy = forms.CharField(max_length=1000, default="")


class UpdateViewForm(forms.ModelForm):
    query_list = User.objects.values_list("first_name", "last_name")
    USER_CHOICES = [i for i in query_list]
    user = forms.ChoiceField(choices = USER_CHOICES)

    class Meta:
        model = Entry
        fields = ("title",
              "detail",
              "user",
              "date_for")
    

        