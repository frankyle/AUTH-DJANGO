# accounts/urls.py
from django.urls import path, include

urlpatterns = [
    path('', include('djoser.urls')),  # Include Djoser endpoints
    path('', include('djoser.urls.jwt')),  # JWT endpoints for token-based authentication
]


