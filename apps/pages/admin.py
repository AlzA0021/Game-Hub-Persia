from django.contrib import admin

from .models import Page


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'published', 'updated_at')
    search_fields = ('title', 'content')
    list_filter = ('published',)
    prepopulated_fields = {'slug': ('title',)}
