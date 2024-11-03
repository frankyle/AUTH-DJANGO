from django.contrib import admin
from django.utils.html import format_html
from .models import CandleImages

@admin.register(CandleImages)
class CandleImagesAdmin(admin.ModelAdmin):
    # Display these fields in the list view
    list_display = (
        'trade_detail',
        'monday_candle_image',
        'tuesday_candle_image',
        'wednesday_candle_image',
        'thursday_candle_image',
        'friday_candle_image',
        'saturday_candle_image',
        'sunday_candle_image',
        'swing_trade_candle_image'
    )
    
    # Filters to search for specific days or candle types
    list_filter = ('trade_detail',)
    
    # Allow searching by related `TradeDetails` fields
    search_fields = ('trade_detail__currency_pair', 'trade_detail__user__username')
    
    # Group fields in sections
    fieldsets = (
        (None, {
            'fields': ('trade_detail',)
        }),
        ('Day-Specific Candles', {
            'fields': (
                'monday_candle',
                'tuesday_candle',
                'wednesday_candle',
                'thursday_candle',
                'friday_candle',
                'saturday_candle',
                'sunday_candle'
            ),
        }),
        ('Other Candle Types', {
            'fields': ('swing_trade_candle',),
        }),
    )

    # Thumbnail functions for each image field
    def monday_candle_image(self, obj):
        if obj.monday_candle:
            return format_html('<img src="{}" width="50" height="50" />', obj.monday_candle.url)
        return None
    monday_candle_image.short_description = 'Monday Candle'

    def tuesday_candle_image(self, obj):
        if obj.tuesday_candle:
            return format_html('<img src="{}" width="50" height="50" />', obj.tuesday_candle.url)
        return None
    tuesday_candle_image.short_description = 'Tuesday Candle'

    def wednesday_candle_image(self, obj):
        if obj.wednesday_candle:
            return format_html('<img src="{}" width="50" height="50" />', obj.wednesday_candle.url)
        return None
    wednesday_candle_image.short_description = 'Wednesday Candle'

    def thursday_candle_image(self, obj):
        if obj.thursday_candle:
            return format_html('<img src="{}" width="50" height="50" />', obj.thursday_candle.url)
        return None
    thursday_candle_image.short_description = 'Thursday Candle'

    def friday_candle_image(self, obj):
        if obj.friday_candle:
            return format_html('<img src="{}" width="50" height="50" />', obj.friday_candle.url)
        return None
    friday_candle_image.short_description = 'Friday Candle'

    def saturday_candle_image(self, obj):
        if obj.saturday_candle:
            return format_html('<img src="{}" width="50" height="50" />', obj.saturday_candle.url)
        return None
    saturday_candle_image.short_description = 'Saturday Candle'

    def sunday_candle_image(self, obj):
        if obj.sunday_candle:
            return format_html('<img src="{}" width="50" height="50" />', obj.sunday_candle.url)
        return None
    sunday_candle_image.short_description = 'Sunday Candle'

    def swing_trade_candle_image(self, obj):
        if obj.swing_trade_candle:
            return format_html('<img src="{}" width="50" height="50" />', obj.swing_trade_candle.url)
        return None
    swing_trade_candle_image.short_description = 'Swing Trade Candle'
