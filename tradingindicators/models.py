from django.db import models
from tradedetails.models import TradeDetails

class TradingIndicators(models.Model):
    trade_detail = models.ForeignKey(TradeDetails, on_delete=models.CASCADE, related_name="trading_indicators")

    # Pattern and level fields
    candle_pattern = models.CharField(
        max_length=20,
        choices=(
            ("Engulfing", "Engulfing Candle"), 
            ("Small Body", "Small Candle"),
            ("Pinbar", "Pin bar Candle"),
        ),
        blank=True,
        null=True
    )
    fibonacci_level = models.CharField(
        max_length=5,
        choices=(("38.2%", "38.2%"), ("50%", "50%"), ("61.8%", "61.8%"), ("78.6%", "78.6%")),
        blank=True,
        null=True
    )
    session = models.CharField(
        max_length=15,
        choices=(("London", "London Session"), ("Newyork", "New York Session")),
        blank=True,
        null=True
    )

    # Boolean indicators
    five_min_order_block = models.BooleanField(default=False)
    previous_day_color_structure = models.BooleanField(default=False)
    asion_kill_zone = models.BooleanField(default=False)
    london_kill_zone = models.BooleanField(default=False)
    newyork_kill_zone = models.BooleanField(default=False)
    flip_four_hour_candle = models.BooleanField(default=False)
    fifteen_min_break_of_structure = models.BooleanField(default=False)
    fvg_blocks = models.BooleanField(default=False)
    change_color_ut_alert = models.BooleanField(default=False)
    flactial_and_alligator = models.BooleanField(default=False)

    # Additional fields for pips
    pips_stoplost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, default=0)
    pips_gained = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, default=0)

    class Meta:
        verbose_name = "Trading indicator"
        verbose_name_plural = "Trading indicators"
