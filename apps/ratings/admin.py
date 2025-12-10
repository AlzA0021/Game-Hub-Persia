from django.contrib import admin

from .models import Rating


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('user', 'game', 'value', 'created_at')
    search_fields = ('user__username', 'game__title')
    list_filter = ('value',)
    autocomplete_fields = ('user', 'game')
