from django.urls import path
from .views import CandleListCreateView

urlpatterns = [
    path('candles/', CandleListCreateView.as_view(), name='candle-list-create'),
]
