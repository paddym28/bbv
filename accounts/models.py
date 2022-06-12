from statistics import mode
from unicodedata import name
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from videos.models import *

# User Profile Model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    username = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)
    phn = models.CharField(max_length=100, null=True)
    dob = models.DateField(null=True)    
    date_created = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name
    

