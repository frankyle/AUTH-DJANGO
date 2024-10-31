from rest_framework import serializers
from .models import TradeDetails

class TradeDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TradeDetails
        fields = '__all__'
