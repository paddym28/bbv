from django.db import models
from datetime import datetime
from authors.models import Author
from django.contrib.auth.models import User

# Category (for video) Model
class Category(models.Model):
    name = models.CharField(max_length=200, null = True)

    def __str__(self):
        return self.name

# Video Model
class Video(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    desciption = models.TextField(blank=True)
    thumb = models.ImageField(upload_to="photos/%Y/%m/%d")
    video_id = models.CharField(max_length=200)
    # video_url = models.FileField(upload_to='videos/%Y/%m/%d', null=True)
    category = models.ManyToManyField(Category)
    is_featured = models.BooleanField(default=False)
    is_latest = models.BooleanField(default=False)
    slide1 = models.BooleanField(default=False)
    slide2 = models.BooleanField(default=False)
    slide3 = models.BooleanField(default=False)
    date_created = models.DateTimeField(default=datetime.now, blank=True)
    
    def __str__(self):
        return self.name

# User Watchlist Model
class UserWatchlist(models.Model):
    user = models.ForeignKey(User , null = False , on_delete=models.CASCADE)
    video = models.ForeignKey(Video , null = False , on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return f'{self.user.username} - {self.video.name}'