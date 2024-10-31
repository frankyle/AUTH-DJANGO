from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TradingIndicatorsViewSet  # Import your viewset

router = DefaultRouter()
router.register(r'tradingindicators', TradingIndicatorsViewSet, basename='tradingindicator')  # Use a basename for consistency

urlpatterns = [
    path('', include(router.urls)),  # No additional path here
]
