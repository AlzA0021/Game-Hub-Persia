from django.db.models import Avg, Count
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Game, Genre, Platform, Release
from .serializers import (
    GameSerializer,
    GenreSerializer,
    PlatformSerializer,
    ReleaseSerializer,
)


class GameViewSet(viewsets.ModelViewSet):
    serializer_class = GameSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'genre', 'developer', 'publisher', 'description']
    ordering_fields = ['created_at', 'release_date', 'title', 'average_rating']

    def get_queryset(self):
        queryset = (
            Game.objects.prefetch_related('genres', 'platforms')
            .annotate(
                average_rating=Avg('ratings__value'),
                rating_count=Count('ratings', distinct=True),
                review_count=Count('reviews', distinct=True),
                favorites_count=Count('favorites', distinct=True),
            )
        )

        genre_slug = self.request.query_params.get('genre')
        platform_slug = self.request.query_params.get('platform')
        if genre_slug:
            queryset = queryset.filter(genres__slug=genre_slug)
        if platform_slug:
            queryset = queryset.filter(platforms__slug=platform_slug)
        return queryset.distinct()


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'description']
    ordering_fields = ['name']
    lookup_field = 'slug'


class PlatformViewSet(viewsets.ModelViewSet):
    queryset = Platform.objects.all()
    serializer_class = PlatformSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'manufacturer']
    ordering_fields = ['name']
    lookup_field = 'slug'


class ReleaseViewSet(viewsets.ModelViewSet):
    queryset = Release.objects.select_related('game', 'platform').all()
    serializer_class = ReleaseSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['release_date']
