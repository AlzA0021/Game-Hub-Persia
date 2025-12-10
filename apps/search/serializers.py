from rest_framework import serializers

from apps.games.serializers import GameSerializer
from apps.news.serializers import NewsArticleSerializer
from apps.reviews.serializers import ReviewSerializer


class SearchResultsSerializer(serializers.Serializer):
    query = serializers.CharField()
    games = GameSerializer(many=True)
    news = NewsArticleSerializer(many=True)
    reviews = ReviewSerializer(many=True)
