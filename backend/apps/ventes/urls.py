"""URL routes for ventes app."""
from rest_framework.routers import DefaultRouter

from .views import VenteViewSet

router = DefaultRouter()
router.register(r"", VenteViewSet, basename="ventes")

urlpatterns = router.urls
