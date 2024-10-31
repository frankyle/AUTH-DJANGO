from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CandleImagesViewSet  # Import your viewset

router = DefaultRouter()
router.register(r'candleimages', CandleImagesViewSet, basename='candleimage')  # Use a basename for consistency

urlpatterns = [
    path('', include(router.urls)),  # No additional path here
]