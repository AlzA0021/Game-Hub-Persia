from rest_framework.routers import DefaultRouter

from .views import GameViewSet, GenreViewSet, PlatformViewSet, ReleaseViewSet

router = DefaultRouter()
router.register(r'games', GameViewSet, basename='game')
router.register(r'genres', GenreViewSet, basename='genre')
router.register(r'platforms', PlatformViewSet, basename='platform')
router.register(r'releases', ReleaseViewSet, basename='release')

urlpatterns = router.urls
