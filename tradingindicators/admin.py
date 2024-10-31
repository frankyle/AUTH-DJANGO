from django.contrib import admin
from .models import TradingIndicators

@admin.register(TradingIndicators)
class TradingIndicatorsAdmin(admin.ModelAdmin):
    list_display = (
        'trade_detail', 
        'candle_pattern', 
        'fibonacci_level', 
        'session', 
        'five_min_order_block', 
        'previous_day_color_structure', 
        'asion_kill_zone', 
        'london_kill_zone', 
        'newyork_kill_zone', 
        'flip_four_hour_candle', 
        'fifteen_min_break_of_structure', 
        'fvg_blocks', 
        'change_color_ut_alert', 
        'flactial_and_alligator', 
        'pips_stoplost', 
        'pips_gained'
    )
    list_filter = ('candle_pattern', 'fibonacci_level', 'session', 'five_min_order_block', 'london_kill_zone')
    search_fields = ('trade_detail__currency_pair', 'candle_pattern', 'session')
