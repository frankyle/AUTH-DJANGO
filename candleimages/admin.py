from django.contrib import admin
from .models import CandleImages

@admin.register(CandleImages)
class CandleImagesAdmin(admin.ModelAdmin):
    list_display = (
        'trade_detail', 
        'monday_candle', 
        'tuesday_candle', 
        'wednesday_candle', 
        'thursday_candle', 
        'friday_candle', 
        'saturday_candle', 
        'sunday_candle', 
        'swing_trade_candle', 
        'two_hour_candle', 
        'breakeven_candle'
    )
    list_filter = ('trade_detail__currency_pair',)  # Filter by currency_pair in the related TradeDetails model
    search_fields = ('trade_detail__currency_pair',)  # Search by currency_pair from TradeDetails
