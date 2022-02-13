import datetime

from django.db import models
from django.utils import timezone
from django.contrib import admin



# Create your models here.

class Squaresy(models.Model):
    square_text = models.CharField(max_length=200)
    number = models.IntegerField(default=0)
    def __str__(self):
        return self.square_text

class Number(models.Model):
    wardle = models.TextField(null=True)
    sessiony = models.CharField(max_length=1000, default="", null=True)
    def __str__(self):
        return self.wardle

class Exceppo(models.Model):
    exceppy = models.TextField(null=True)
    sessiony = models.CharField(max_length=1000, default="", null=True)
    def __str__(self):
        return self.exceppy

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

class Times(models.Model):
    start_time = models.DateTimeField(default=timezone.now)
    finish_time = models.DateTimeField(default=timezone.now)
    attempts = models.IntegerField(default=0)
    sessiony = models.CharField(max_length=1000, default="", null=True)
    def __datetime__(self):
        return self.start_time
