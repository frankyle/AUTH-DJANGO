# profiles/views.py
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import UpdateView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Profile
from .serializers import ProfileSerializer
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt  # Disable CSRF protection for this view
class UpdateUserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self):
        user = self.request.user
        return get_object_or_404(Profile, user=user)

    def patch(self, request, *args, **kwargs):
        profile = self.get_object()
        serializer = ProfileSerializer(profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


class ProfileEditView(UpdateView):
    model = Profile
    template_name = 'profiles/edit_profile.html'

    def get_object(self, queryset=None):
        return get_object_or_404(Profile, user=self.request.user)

    def get_success_url(self):
        return reverse('profile_detail', kwargs={'pk': self.object.pk})
