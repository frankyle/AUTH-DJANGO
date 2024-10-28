from rest_framework import generics
from .models import Candle
from .serializers import CandleSerializer
from rest_framework.permissions import IsAuthenticated

class CandleListCreateView(generics.ListCreateAPIView):
    queryset = Candle.objects.all()
    serializer_class = CandleSerializer
    permission_classes = [IsAuthenticated]
