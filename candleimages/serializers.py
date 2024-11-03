from rest_framework import serializers
from .models import CandleImages

class CandleImagesSerializer(serializers.ModelSerializer):
    currency_pair = serializers.CharField(source='trade_detail.currency_pair', read_only=True)

    class Meta:
        model = CandleImages
        fields = '__all__'
