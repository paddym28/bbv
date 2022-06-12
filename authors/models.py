from django.db import models
from datetime import datetime

# Author Model
class Author(models.Model):
    username = models.CharField(max_length=200, null=True)
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d")
    short_intro = models.TextField(blank=False)
    bio = models.TextField(blank=False)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=500)
    social_twitter = models.CharField(max_length=200, blank=True)
    social_youtube = models.CharField(max_length=200, blank=True)
    date_created = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.name
    
    
    
