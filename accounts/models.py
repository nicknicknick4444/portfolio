from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    short_name = models.CharField(max_length=3, unique=True)
