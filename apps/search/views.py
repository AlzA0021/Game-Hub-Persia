from rest_framework.views import APIView
from rest_framework.response import Response

from apps.games.models import Game
from apps.news.models import NewsArticle
from apps.reviews.models import Review
from .serializers import SearchResultsSerializer


class GlobalSearchView(APIView):
    def get(self, request):
        query = request.query_params.get('q', '').strip()
        games = Game.objects.none()
        news = NewsArticle.objects.none()
        reviews = Review.objects.none()

        if query:
            games = Game.objects.filter(title__icontains=query)[:5]
            news = NewsArticle.objects.filter(title__icontains=query)[:5]
            reviews = Review.objects.filter(body__icontains=query)[:5]

        serializer = SearchResultsSerializer({
            'query': query,
            'games': games,
            'news': news,
            'reviews': reviews,
        })
        return Response(serializer.data)
