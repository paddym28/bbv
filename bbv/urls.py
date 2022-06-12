
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Included Pages App Url
    path('', include('pages.urls')),
    
    # Included Videos App Url
    path('videos/', include('videos.urls')),
    
    # Included Authors App Url
    path('authors/', include('authors.urls')),
    
    # Included Accounts App Url
    path('accounts/', include('accounts.urls')),
    
    # Admin Url
    path('admin/', admin.site.urls),
    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
