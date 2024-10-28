from django.urls import path
from profiles import views as profile_views

urlpatterns = [
    path('edit/', profile_views.ProfileEditView.as_view(), name='profile_edit'),
    # Add other profile-related URL patterns as needed
]
