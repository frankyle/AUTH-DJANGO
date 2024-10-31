from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import CandleImages
from .serializers import CandleImagesSerializer
from rest_framework.permissions import IsAuthenticated

class CandleImagesViewSet(viewsets.ModelViewSet):
    queryset = CandleImages.objects.all()
    serializer_class = CandleImagesSerializer
    permission_classes = [IsAuthenticated] 

    def create(self, request):
        request.data['trade_detail'] = request.data.get('trade_detail')  # Assuming you provide the trade_detail ID

        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
