from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from accounts.views import *
from .models import *

from django.db.models import Q
from .utils import searchVideos 
from django.contrib.auth.decorators import login_required


# Videos View
def index(request):
    
    # Pagination
    videos, search_query = searchVideos(request)
    
    page = request.GET.get('page')
    paginator = Paginator(videos, 4)
    paged_videos = paginator.get_page(page)
    
    
    try:
        videos = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        videos = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        videos = paginator.page(page)
        
    context = {
        'videos' : paged_videos,
        'search_query' : search_query,
    }
    return render(request, 'videos/videos.html', context)

# Single Video View
def video(request, video_id):
    video = get_object_or_404(Video, pk = video_id)
    context = {
        'video' : video
    }
    return render(request, 'videos/video.html', context)

# Play Video Url
@login_required(login_url = 'loginContinue')
def playVideo(request, pk ):
    
    video = Video.objects.get(id = pk)
    user = request.user
    
    # Watchlist Functionality
    if request.method == 'POST':     
        try:
            user_watchlist = UserWatchlist.objects.get(user = user  , video = video)
            messages.info(request, 'That Video already exists in watchlist' )
        except:
            user_watchlist = UserWatchlist(user = user , video = video)            
            user_watchlist.save()
            messages.info(request, 'Video is added in watchlist' )
    context = {
        'video' : video,
        
    }
    return render(request, 'videos/play_video.html', context)

# Search View
def search(request):
    videos, search_query = searchVideos(request)
    
    
    context = {
        'videos' : videos,
        'search_query' : search_query,
    }
    return render(request, 'videos/search.html', context)

# Short Story View
def shortStory(request):
    video = Video.objects.filter(category__name = 'Short Stories')
    context = {
        'videos' : video
    }
    return render(request, 'videos/short_story.html' , context)

# Mythology View
def mythology(request):
    video = Video.objects.filter(category__name = 'Mythology')
    context = {
        'videos' : video
    }
    return render(request, 'videos/mythology.html', context )

# Motivation View
def motivation(request):
    video = Video.objects.filter(category__name = 'Motivation')
    context = {
        'videos' : video
    }
    return render(request, 'videos/motivation.html', context )

# Sel Improvement
def selfImprovement(request):
    video = Video.objects.filter(category__name = 'Self Improvement')
    context = {
        'videos' : video
    }
    return render(request, 'videos/self_improvement.html' , context)