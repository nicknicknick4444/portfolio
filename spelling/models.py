import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Tub(models.Model):
    the_text = models.CharField(max_length=200, default="")
    def __str__(self):
        return self.the_text

class Admonish(models.Model):
    adm_id = models.IntegerField(default=0)
    adm_term = models.CharField(max_length=200, default="")
    adm_text = models.CharField(max_length=280, default="")
    #adm_seshn = models.CharField(max_length=200, default="")
    def __str__(self):
        return self.adm_text

class TweetLists(models.Model):
    twe_dict = models.CharField(max_length=5000, default="")
    twe_term = models.CharField(max_length=20, default="")
    twe_seshn = models.CharField(max_length=200, default="")
    #twe_time = models.DateTimeField(default=datetime.datetime.now(datetime.timezone.utc))
    twe_time = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.twe_seshn
