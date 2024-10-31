from django.contrib import admin
from .models import TradeDetails

@admin.register(TradeDetails)
class TradeDetailsAdmin(admin.ModelAdmin):
    list_display = (
        'user', 
        'currency_pair', 
        'trade_signal', 
        'is_active', 
        'created_at', 
        'idea_candle', 
        'line_graph_candle', 
        'signal_candle', 
        'hour_candle', 
        'entry_candle', 
        'take_profit_one_candle', 
        'take_profit_two_candle'
    )
    list_filter = ('trade_signal', 'is_active', 'created_at')
    search_fields = ('user__username', 'currency_pair')
