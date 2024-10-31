from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TradeDetailsViewSet  # Import your viewset

router = DefaultRouter()
router.register(r'tradedetails', TradeDetailsViewSet, basename='tradedetail')  # Use a basename for consistency

urlpatterns = [
    path('', include(router.urls)),  # No additional path here
]
