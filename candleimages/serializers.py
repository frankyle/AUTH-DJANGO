from rest_framework import serializers
from .models import CandleImages

class CandleImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CandleImages
        fields = '__all__'
