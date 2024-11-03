from django.db import models
from tradedetails.models import TradeDetails

class CandleImages(models.Model):
    trade_detail = models.ForeignKey(TradeDetails, on_delete=models.CASCADE, related_name="candle_images")

    # Day-specific candles
    monday_candle = models.ImageField(upload_to='monday_candles/', null=True, blank=True)
    tuesday_candle = models.ImageField(upload_to='tuesday_candles/', null=True, blank=True)
    wednesday_candle = models.ImageField(upload_to='wednesday_candles/', null=True, blank=True)
    thursday_candle = models.ImageField(upload_to='thursday_candles/', null=True, blank=True)
    friday_candle = models.ImageField(upload_to='friday_candles/', null=True, blank=True)
    saturday_candle = models.ImageField(upload_to='saturday_candles/', null=True, blank=True)
    sunday_candle = models.ImageField(upload_to='sunday_candles/', null=True, blank=True)

    # Other candle types
    swing_trade_candle = models.ImageField(upload_to='swing_trade_candle/', null=True, blank=True)

    class Meta:
        verbose_name = "Candle image"
        verbose_name_plural = "Candle images"
