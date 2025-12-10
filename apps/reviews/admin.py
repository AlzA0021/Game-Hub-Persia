from django.contrib import admin

from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'game', 'rating', 'created_at')
    search_fields = ('game__title', 'user__username')
    list_filter = ('rating',)
    autocomplete_fields = ('user', 'game')
