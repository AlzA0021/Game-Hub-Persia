from django.contrib import admin

from .models import NewsArticle


@admin.register(NewsArticle)
class NewsArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'game', 'author', 'published_at')
    search_fields = ('title', 'content')
    list_filter = ('published_at',)
    prepopulated_fields = {'slug': ('title',)}
