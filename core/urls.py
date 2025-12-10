from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.accounts.urls import router as accounts_router
from apps.games.urls import router as games_router
from apps.news.urls import router as news_router
from apps.reviews.urls import router as reviews_router
from apps.ratings.urls import router as ratings_router
from apps.interactions.urls import router as interactions_router
from apps.pages.urls import router as pages_router
from apps.search.urls import urlpatterns as search_urls
from apps.pages import site_views

router = DefaultRouter()
for app_router in [
    accounts_router,
    games_router,
    news_router,
    reviews_router,
    ratings_router,
    interactions_router,
    pages_router,
]:
    for prefix, viewset, basename in app_router.registry:
        router.registry.append((prefix, viewset, basename))

urlpatterns = [
    path('', site_views.HomeView.as_view(), name='home'),
    path('games/', site_views.GameListView.as_view(), name='games'),
    path('games/<slug:slug>/', site_views.GameDetailView.as_view(), name='game-detail'),
    path('news/', site_views.NewsListView.as_view(), name='news'),
    path('news/<slug:slug>/', site_views.NewsDetailView.as_view(), name='news-detail'),
    path('reviews/', site_views.ReviewListView.as_view(), name='reviews'),
    path('reviews/<int:pk>/', site_views.ReviewDetailView.as_view(), name='review-detail'),
    path('releases/', site_views.ReleaseCalendarView.as_view(), name='releases'),
    path('genres/', site_views.GenreListView.as_view(), name='genres'),
    path('platforms/', site_views.PlatformListView.as_view(), name='platforms'),
    path('search/', site_views.SearchView.as_view(), name='search'),
    path('pages/<slug:slug>/', site_views.PageDetailView.as_view(), name='page-detail'),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
] + search_urls
