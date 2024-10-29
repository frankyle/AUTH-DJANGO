from rest_framework import serializers
from djoser.serializers import UserSerializer
from .models import UserAccount


class UserAccountSerializer(UserSerializer):
    class Meta:
        model = UserAccount
        fields = ('id', 'email', 'first_name', 'last_name')  # Only include core User fields

    def create(self, validated_data):
        # Create the UserAccount instance
        user = UserAccount.objects.create_user(**validated_data)

        # Create the Profile instance linked to the User
        profile = Profile.objects.create(user=user)

        # Additional logic for profile creation (optional)
        # ...

        return user
    
    
    