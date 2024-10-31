from rest_framework import serializers
from .models import TradingIndicators

class TradingIndicatorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TradingIndicators
        fields = '__all__'
