from django.urls import path
from . import views

urlpatterns = [
    # Login Url
    path('login', views.login, name='login'),
    # Register Url
    path('register', views.register, name='register'),
    # Logout Url
    path('logout', views.logout, name='logout'),
    # Dashboard Url
    path('dashboard', views.dashboard, name='dashboard'),
    # Watchlist Url
    path('watchlist', views.watchlist, name='watchlist'),
    # Edit Profile Url
    path('edit-account', views.editAccount, name='edit-account'),
    # Login Required Url
    path('continue', views.loginContinue, name='loginContinue'),  
]
