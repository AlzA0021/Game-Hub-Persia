from django.urls import path

from .views import GlobalSearchView

urlpatterns = [
    path('api/search/', GlobalSearchView.as_view(), name='global-search'),
]

# expose empty router for compatibility
class DummyRouter:
    registry = []

router = DummyRouter()
