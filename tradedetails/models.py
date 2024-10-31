from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class TradeDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    currency_pair = models.CharField(max_length=6, null=True, blank=True)
    trade_signal = models.CharField(max_length=4, choices=(("buy", "Buy"), ("sell", "Sell")), null=True, blank=True)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    # Hour and custom candles
    idea_candle = models.ImageField(upload_to='idea_candles/', null=True, blank=True)
    line_graph_candle = models.ImageField(upload_to='line_graph_candles/', null=True, blank=True)
    signal_candle = models.ImageField(upload_to='signal_candles/', null=True, blank=True)
    hour_candle = models.ImageField(upload_to='hour_candles/', null=True, blank=True)
    entry_candle = models.ImageField(upload_to='entry_candle/', null=True, blank=True)

    # Take profit candles
    take_profit_one_candle = models.ImageField(upload_to='take_profit_one_candle/', null=True, blank=True)
    take_profit_two_candle = models.ImageField(upload_to='take_profit_two_candle/', null=True, blank=True)

    class Meta:
        verbose_name = "Trade detail"
        verbose_name_plural = "Trade details"
