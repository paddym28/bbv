from django.shortcuts import render, redirect
from authors.models import Author
from .models import *
from .forms import ContactForm
from videos.models import *
# Create your views here.

# Index View
def index(request):
    
    # Query For Featured Video
    featured = Video.objects.all().filter(is_featured = True)
    
    # Query for Latest Video
    latest = Video.objects.all().filter(is_latest = True)
    
    # Query for Home Page slider
    slide1 =  Video.objects.filter(slide1 = True)
    slide2 =  Video.objects.filter(slide2 = True)
    slide3 =  Video.objects.filter(slide3 = True)
    
    context = {
        'featured' : featured,
        'latest' : latest, 
        'slide1' : slide1,
        'slide2' : slide2,
        'slide3' : slide3,
    }
    return render(request, 'pages/index.html', context)

# About View
def about(request): 
    return render(request, 'pages/about.html')

# Contact View
def contact(request):
     
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(contact)
    
    context ={
        'form': form
    }
    return render(request, 'pages/contact.html', context)
    