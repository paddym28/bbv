from django.urls import path
from . import views

urlpatterns = [
    # Index Url
    path('', views.index, name='index'),
    
    # About Url
    path('about', views.about, name='about'),
    
    # Contact Url
    path('contact', views.contact, name='contact'),
    
]
