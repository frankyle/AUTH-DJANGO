from django.contrib import admin
from django.urls import path, include
from profiles import urls as profile_urls  # Correct import of profile URLs

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('accounts.urls')),  # URLs for user management
    path('profile/', include(profile_urls)),  # URLs for user profiles
    path('mgicandles/', include('mgicandles.urls')),  # Include mgicandles URLs
]
