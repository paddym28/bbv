from django.contrib import admin
from .models import Author

# Author Admin Area
class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'email',
        'phone',
    )
    list_display_links = ('id', 'name',)
    list_filter = ('name',)
    search_fields = ('name', 'description', 'short_intro', )
    list_per_page = 10
    
admin.site.register(Author, AuthorAdmin)
