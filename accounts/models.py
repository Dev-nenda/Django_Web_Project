# accounts/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    phone_number = models.CharField(max_length= 11)
    stars = models.ManyToManyField('self', symmetrical=False, related_name='fans')    

    


