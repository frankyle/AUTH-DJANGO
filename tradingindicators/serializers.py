from rest_framework import serializers
from .models import TradingIndicators

class TradingIndicatorsSerializer(serializers.ModelSerializer):
    currency_pair = serializers.CharField(source='trade_detail.currency_pair', read_only=True)

    class Meta:
        model = TradingIndicators
        fields = '__all__'
