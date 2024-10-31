from django.contrib import admin
from .models import MgiCandles

@admin.register(MgiCandles)
class MgiCandlesAdmin(admin.ModelAdmin):
    # List view settings
    list_display = (
        'user', 
        'currency_pair', 
        'trade_signal', 
        'is_active', 
        'created_at',
        'pips_stoplost', 
        'pips_gained', 
        'candle_pattern', 
        'fibonacci_level', 
        'session'
    )
    list_filter = (
        'is_active', 
        'trade_signal', 
        'candle_pattern', 
        'fibonacci_level', 
        'session', 
        'created_at'
    )
    search_fields = ('user__username', 'currency_pair', 'trade_signal', 'session')
    
    # Sectioned fieldsets for better organization
    fieldsets = (
        ('General Information', {
            'fields': ('user', 'currency_pair', 'trade_signal', 'is_active', 'created_at')
        }),
        ('Performance Metrics', {
            'fields': ('pips_stoplost', 'pips_gained')
        }),
        ('Trade Characteristics', {
            'fields': ('candle_pattern', 'fibonacci_level', 'session')
        }),
        ('Image Fields - Trade Candles', {
            'fields': ('idea_candle', 'line_graph_candle', 'signal_candle', 'two_hour_candle')
        }),
        ('Image Fields - Daily Candles', {
            'fields': (
                'monday_candle', 'tuesday_candle', 'wednesday_candle', 
                'thursday_candle', 'friday_candle', 'saturday_candle', 'sunday_candle'
            )
        }),
        ('Image Fields - Additional Candles', {
            'fields': (
                'hour_candle', 'entry_candle', 'breakeven_candle', 
                'take_profit_one_candle', 'take_profit_two_candle', 'swing_trade_candle'
            )
        }),
        ('Additional Flags and Indicators', {
            'fields': (
                'five_min_order_block', 'previous_day_color_structure', 'asian_kill_zone', 
                'london_kill_zone', 'newyork_kill_zone', 'flip_four_hour_candle', 
                'fifteen_min_break_of_structure', 'fvg_blocks', 'change_color_ut_alert', 
                'fractal_and_alligator'
            )
        }),
    )

    # Optional: To make images editable as previews in admin
    readonly_fields = ('created_at',)
