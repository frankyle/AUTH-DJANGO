from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import TradeDetails
from .serializers import TradeDetailsSerializer
from rest_framework.permissions import IsAuthenticated

class TradeDetailsViewSet(viewsets.ModelViewSet):
    queryset = TradeDetails.objects.all()
    serializer_class = TradeDetailsSerializer
    permission_classes = [IsAuthenticated] 

    def create(self, request):
        request.data['user'] = request.user.id

        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
