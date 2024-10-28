from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    nationality = models.CharField(max_length=50, blank=True, null=True)
    region = models.CharField(max_length=50, blank=True, null=True)
    image = models.ImageField(upload_to='profile_images/', blank=True)  # Using Pillow library for images
    age = models.PositiveIntegerField(blank=True, null=True)
    informed_by = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.user.email}'s Profile"
    
    