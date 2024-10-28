from rest_framework import serializers
from .models import Candle

class CandleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candle
        fields = '__all__'
