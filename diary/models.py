import datetime

from django.db import models
from django.core.exceptions import ValidationError
from django.urls import reverse
from datetime import date

# Create your models here.

class Entry(models.Model):
    title = models.CharField(max_length=250)
    detail = models.CharField(max_length=1000)
    user = models.CharField(max_length=100)
    by = models.CharField(max_length=100, default="")
    created = models.DateField()
    last_modified = models.DateField()
    date_for = models.DateField()
    
    def clean(self, *args, **kwargs):
        super(Entry, self).clean(*args, **kwargs)
        if self.date_for < datetime.datetime.now().date():
            raise ValidationError("Date can't be in the past!")
        #print(self.date_for < datetime.datetime.now().date() - 1)
    @property
    def is_old(self):
        return self.date_for < datetime.datetime.now().date()
            

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("diary:home")
    
class SendTime(models.Model):
    send_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.send_time
    
#     def get_absolute_url(self):
#         return reverse(
#             )