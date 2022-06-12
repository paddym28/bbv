from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from videos.models import *
from videos.views import *
from authors.models import Author
from .models import *
from .forms import *

# Register View
def register(request):
    if request.method == 'POST':
        # Register User
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        # Check if password match
        
        if password == password2:
            # Check Username
            if User.objects.filter(username = username).exists():
                messages.error(request, 'That Username is taken!' )
                return redirect('register')
            else:
                # Check Email
                if User.objects.filter(email = email).exists():
                    messages.error(request, 'That Email Already Exist!' )
                    return redirect('register')
                else:
                    # Create User
                    user = User.objects.create_user(
                        first_name = first_name,
                        last_name = last_name,
                        username = username,
                        email = email,
                        password = password
                    )
                # Login after register
                    # auth.login(request,user)
                    # messages.success(request, 'You are now Logged In!')
                    # return redirect('index')
                user.save()
                messages.success(request, 'You are now Registered! Can Login ')
                return redirect('login')
        else:
            messages.error(request, "Passwords Do Not Match!" )
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')

# Login View
def login(request):
    if request.method == 'POST':
        # Login User
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username = username, password =password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('login')
        
    else:
        return render(request, 'accounts/login.html')

# Logout User
def logout(request):
        auth.logout(request)
        return redirect('index')

# Login Required View
def loginContinue(request):
    return render(request, 'accounts/continue.html')
      

# Dashboard View
@login_required(login_url='loginContinue')
def dashboard(request):
    
    account = request.user.profile
    user = request.user
    
    # Query For Featured Videos
    featured = Video.objects.all().filter(is_featured = True)
    
    # Query For Latest Video
    latest = Video.objects.all().filter(is_latest = True)
    
    # Query For Uploaded Video, Checks whether Author's username matches with logged in user's username
    uploaded = Video.objects.all().filter(author__username = user.username)
    
    # Query for Home Page Slider
    slide1 =  Video.objects.filter(slide1 = True)
    slide2 =  Video.objects.filter(slide2 = True)
    slide3 =  Video.objects.filter(slide3 = True)
    
    context = {
        'account' : account,
        'featured' : featured,
        'latest' : latest,
        'uploaded' : uploaded,
        'slide1' : slide1,
        'slide2' : slide2,
        'slide3' : slide3,    
    }
    return render(request, 'accounts/dashboard.html', context)

# Watchlist View
@login_required(login_url='loginContinue')
def watchlist(request):   
    user = request.user
    
    # Query For getting logged in User's Watchlist
    user_watchlist = UserWatchlist.objects.filter(user = user)
    
    context = {
        'user_watchlist' : user_watchlist,
    }
    return render(request, 'accounts/watchlist.html', context )

# Edit Profile View
@login_required(login_url='loginContinue')
def editAccount(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)
    
    if request.method == 'POST':
        form = ProfileForm(request.POST,instance=profile)
        if form.is_valid():
            form.save()

            return redirect('account')
        
    context = {
    }
    return render(request, 'accounts/edit-account.html', context)


