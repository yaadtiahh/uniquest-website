from django.contrib import admin
from .models import News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_date', 'is_visible')
    list_editable = ('is_visible',)
    search_fields = ('title', 'description')
    list_filter = ('is_visible', 'published_date')
