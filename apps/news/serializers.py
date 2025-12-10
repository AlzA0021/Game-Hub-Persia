from rest_framework import serializers

from .models import NewsArticle


class NewsArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsArticle
        fields = ['id', 'title', 'slug', 'content', 'game', 'author', 'published_at']
        read_only_fields = ['id', 'slug', 'published_at']
