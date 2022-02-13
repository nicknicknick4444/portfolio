import datetime

from django.db import models
from django.utils import timezone
from django.contrib import admin



# Create your models here.

# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField("date published")
#     
#     def __str__(self):
#         return self.question_text
#     @admin.display(
#         boolean=True,
#         ordering="pub_date",
#         description="Recent?",
#         )
#     def was_published_recently(self):
#         now = timezone.now()
#         return now - datetime.timedelta(days=1) <= self.pub_date <= now

# class Choice(models.Model):
#     question = models.ForeignKey(
#         Question,
#         on_delete = models.CASCADE
#         )
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)
#     
#     def __str__(self):
#         return self.choice_text
    

class Squaresy(models.Model):
    square_text = models.CharField(max_length=200)
    number = models.IntegerField(default=0)
    #game_list = models.TextField(null=True)
    def __str__(self):
        return self.square_text

class Number(models.Model):
    #the_except = models.TextField(null=True)
    #game_list = models.TextField(null=True)
    #game_list2, the_except2 = make_list_for_view()
    wardle = models.TextField(null=True)
    sessiony = models.CharField(max_length=1000, default="", null=True)
    #initial_cou = initial_cou(game_list2)
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
