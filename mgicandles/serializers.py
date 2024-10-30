from rest_framework import serializers
from .models import MgiCandles

class MgiCandlesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MgiCandles
        fields = '__all__'
