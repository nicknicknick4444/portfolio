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
User._meta.get_field("last_name")._unique = True
User._meta.get_field("first_name").verbose_name = "Nickname"
User._meta.get_field("last_name").verbose_name = "Initial"
User._meta.get_field("first_name").blank = False
User._meta.get_field("last_name").blank = False
User._meta.get_field("email").blank = False

def get_user_choices():
    user_query = User.objects.values_list("first_name","last_name")
    USER_CHOICES = [i for i in user_query]
    return USER_CHOICES

class Entry(models.Model):
    user_query = User.objects.values_list("first_name", "last_name")
    USER_CHOICES = [i for i in user_query]
    
    title = models.CharField(max_length=250)
    detail = models.CharField(max_length=1000)
    
    by = models.CharField(max_length=100, default="")
    mod_by = models.CharField(max_length=100, default="")
    user = models.CharField(max_length=20, choices = get_user_choices(), blank=False, default="")

    created = models.DateField()
    last_modified = models.DateField()
    date_for = models.DateField()
        
    def clean(self, *args, **kwargs):
        super(Entry, self).clean(*args, **kwargs)
        if self.date_for < datetime.datetime.now().date():
            raise ValidationError("Date can't be in the past!")
    @property
    def is_old(self):
        return self.date_for < datetime.datetime.now().date()
    
    def get_absolute_url(self):
        return reverse("diary:home")
    
class SendTime(models.Model):
    send_time = models.CharField(max_length=100, default="00:00")
    
    def __str__(self):
        return self.send_time
