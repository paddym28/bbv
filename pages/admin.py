from django.contrib import admin
from .models import *

# Contact Admin Area
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'email',
    )
    list_display_links = ('id', 'name',)
    list_filter = ('name', 'email', )
    search_fields = ('name', 'email', 'message', )
    list_per_page = 10

admin.site.register(Contact, ContactAdmin )