from django.shortcuts import render
from .models import Author
from videos.models import *

# Author View
def index(request, pk ):
    authors = Author.objects.get(id=pk)
    context = {
        'author' : authors
    }
    return render(request, 'authors/author.html', context)

