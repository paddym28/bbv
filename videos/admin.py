from django.contrib import admin
from .models import Video, Category

# Video Admin Area
class VideoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'author',
        'is_featured',
        'is_latest',
        'slide1',
        'slide2',
        'slide3',
    )
    list_display_links = ('id', 'name',)
    list_filter = ('author', 'category', )
    list_editable = ('is_featured','is_latest', 'slide1', 'slide2', 'slide3')
    search_fields = ('name', 'category', 'author', 'description', )
    list_per_page = 10
admin.site.register(Video,VideoAdmin)
admin.site.register(Category)

