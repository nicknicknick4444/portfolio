import datetime

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date

# Create your models here.

User._meta.get_field("first_name")._unique = True

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=CASCADE)

#MY = [("a","Yes"),("b","No"),("c","maybe"), ("d","Fat chance")]
user_query = User.objects.values_list("first_name","last_name")
USER_CHOICES = [i for i in user_query]
print(USER_CHOICES)

class Entry(models.Model):
    title = models.CharField(max_length=250)
    detail = models.CharField(max_length=1000)
    #user = models.CharField(max_length=100)
    by = models.CharField(max_length=100, default="")
    user = models.CharField(max_length=5, choices = USER_CHOICES)
    #user = models.OneToOneField(User, to_field="first_name", on_delete=models.CASCADE)
    ###user = models.ForeignKey(User, on_delete=models.CASCADE)
    #user = models.ModelMultipleChoiceField(queryset=Users.objects.all())
    #user = models.ForeignKey(User, related_name="first_names", on_delete=models.CASCADE)
    #initial = user.first_name
    ##user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    created = models.DateField()
    last_modified = models.DateField()
    date_for = models.DateField()
    
#     class Meta:
#         db_table = "User"
    
#     def __str__(self):
#         return self.user.username
        #user.get_short_name()
    
    def clean(self, *args, **kwargs):
        super(Entry, self).clean(*args, **kwargs)
        if self.date_for < datetime.datetime.now().date():
            raise ValidationError("Date can't be in the past!")
        #print(self.date_for < datetime.datetime.now().date() - 1)
    @property
    def is_old(self):
        return self.date_for < datetime.datetime.now().date()
            

#     def __str__(self):
#         return self.title
    
    def get_absolute_url(self):
        return reverse("diary:home")

# class Initial(models.Model):
#     models.CharField(max_length=5, unique=True)
    
class SendTime(models.Model):
    send_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.send_time
    
#     def get_absolute_url(self):
#         return reverse(
#             )