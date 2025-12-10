from rest_framework import serializers

from .models import Game, Genre, Platform, Release


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name', 'slug', 'description']
        read_only_fields = ['id', 'slug']


class PlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platform
        fields = ['id', 'name', 'slug', 'manufacturer']
        read_only_fields = ['id', 'slug']


class GameSerializer(serializers.ModelSerializer):
    genres = serializers.SlugRelatedField(
        slug_field='slug', many=True, queryset=Genre.objects.all(), required=False
    )
    platforms = serializers.SlugRelatedField(
        slug_field='slug', many=True, queryset=Platform.objects.all(), required=False
    )
    average_rating = serializers.FloatField(read_only=True)
    rating_count = serializers.IntegerField(read_only=True)
    review_count = serializers.IntegerField(read_only=True)
    favorites_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Game
        fields = [
            'id',
            'title',
            'slug',
            'description',
            'genre',
            'developer',
            'publisher',
            'release_date',
            'genres',
            'platforms',
            'average_rating',
            'rating_count',
            'review_count',
            'favorites_count',
            'created_at',
            'updated_at',
        ]
        read_only_fields = [
            'id',
            'slug',
            'average_rating',
            'rating_count',
            'review_count',
            'favorites_count',
            'created_at',
            'updated_at',
        ]
        extra_kwargs = {'slug': {'required': False}}


class ReleaseSerializer(serializers.ModelSerializer):
    game = serializers.SlugRelatedField(slug_field='slug', queryset=Game.objects.all())
    platform = serializers.SlugRelatedField(slug_field='slug', queryset=Platform.objects.all())

    class Meta:
        model = Release
        fields = ['id', 'game', 'platform', 'region', 'release_date']
        read_only_fields = ['id']
