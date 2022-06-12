from django.db.models import Q
from .models import *
from authors.models import *

def searchVideos(request):
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
        
    category = Category.objects.filter(name__icontains=search_query)
    
    videos = Video.objects.distinct().filter(
        Q(name__icontains=search_query) |
        Q(category__in=category) |
        Q(author__name__icontains=search_query)
    )
    
    return videos, search_query