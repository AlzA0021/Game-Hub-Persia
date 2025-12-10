from django.views.generic import TemplateView, ListView, DetailView
from django.db.models import Q

from apps.games.models import Game, Release, Genre, Platform
from apps.news.models import NewsArticle
from apps.reviews.models import Review
from .models import Page


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_games'] = Game.objects.order_by('-created_at')[:6]
        context['latest_news'] = NewsArticle.objects.order_by('-published_at')[:4]
        context['latest_reviews'] = Review.objects.order_by('-created_at')[:4]
        return context


class GameListView(ListView):
    model = Game
    paginate_by = 12
    template_name = 'games/list.html'

    def get_queryset(self):
        queryset = Game.objects.prefetch_related('genres', 'platforms')
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(title__icontains=query)
        return queryset


class GameDetailView(DetailView):
    model = Game
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    template_name = 'games/detail.html'


class NewsListView(ListView):
    model = NewsArticle
    paginate_by = 10
    template_name = 'news/list.html'


class NewsDetailView(DetailView):
    model = NewsArticle
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    template_name = 'news/detail.html'


class ReviewListView(ListView):
    model = Review
    paginate_by = 10
    template_name = 'reviews/list.html'


class ReviewDetailView(DetailView):
    model = Review
    template_name = 'reviews/detail.html'


class ReleaseCalendarView(ListView):
    model = Release
    template_name = 'releases/calendar.html'
    ordering = ['release_date']


class GenreListView(ListView):
    model = Genre
    template_name = 'genres/list.html'


class PlatformListView(ListView):
    model = Platform
    template_name = 'platforms/list.html'


class SearchView(TemplateView):
    template_name = 'search/results.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('q', '').strip()
        context['query'] = query
        if query:
            context['games'] = Game.objects.filter(title__icontains=query)[:10]
            context['news'] = NewsArticle.objects.filter(title__icontains=query)[:10]
            context['reviews'] = Review.objects.filter(Q(body__icontains=query) | Q(game__title__icontains=query))[:10]
        else:
            context['games'] = Game.objects.none()
            context['news'] = NewsArticle.objects.none()
            context['reviews'] = Review.objects.none()
        return context


class PageDetailView(DetailView):
    model = Page
    template_name = 'pages/detail.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    queryset = Page.objects.filter(published=True)
