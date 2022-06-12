from django.urls import path
from . import views
from authors.views import *

urlpatterns = [
    # All Videos Url
    path('', views.index, name='videos'),
    
    # Single Video Url
    path('<int:video_id>', views.video, name='video'),
    
    # Play Video Url
    path('play/<int:pk>/', views.playVideo, name='play'),
    
    # Search Url
    path('search', views.search, name='search'),
    
    # Short Story Url
    path('short_story', views.shortStory, name= 'shortStory'),
    
    # Mythology Url
    path('mythology', views.mythology, name= 'mythology'),
    
    # Motivation Url
    path('motivation', views.motivation, name= 'motivation'),
    
    # Self Improvement Url
    path('self_improvement', views.selfImprovement, name= 'self_improvement'),
]
