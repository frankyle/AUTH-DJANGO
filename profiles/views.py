from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Profile
from .serializers import ProfileSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request):
        # Automatically associate the profile with the authenticated user
        request.data['user'] = request.user.id
        
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get_queryset(self):
        # Optional: Restrict the queryset to only the authenticated user's profile
        return Profile.objects.filter(user=self.request.user)


