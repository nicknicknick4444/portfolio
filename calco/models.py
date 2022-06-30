from django.db import models

# Create your models here.

class Colour(models.Model):
    colour_name = models.CharField(max_length=20, default="Light Grey")
    colour_hex = models.CharField(max_length=20, default="#D6DBDF")
