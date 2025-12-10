from django.contrib import admin

from .models import Game, Genre, Platform, Release


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'developer', 'publisher', 'release_date')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'developer', 'publisher')
    list_filter = ('release_date',)
    filter_horizontal = ('genres', 'platforms')


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Platform)
class PlatformAdmin(admin.ModelAdmin):
    list_display = ('name', 'manufacturer')
    search_fields = ('name', 'manufacturer')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Release)
class ReleaseAdmin(admin.ModelAdmin):
    list_display = ('game', 'platform', 'region', 'release_date')
    list_filter = ('platform', 'region')
    search_fields = ('game__title', 'platform__name', 'region')
    autocomplete_fields = ('game', 'platform')
