import datetime

from django.db import models
from django.utils import timezone
from django.contrib import admin


# Create your models here.

class Scores(models.Model):
    namey = models.CharField(default="", max_length=9)
    score = models.IntegerField(default=0)
    duration = models.CharField(default = "blank", max_length=30)
    all_seconds = models.IntegerField(default=0)
    attempts = models.IntegerField(default=0)
    def __str__(self):
        return self.namey
    
    def get_duration(self):
        return self.finish_time - self.start_time
