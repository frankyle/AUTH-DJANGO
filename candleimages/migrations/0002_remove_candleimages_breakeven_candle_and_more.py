# Generated by Django 5.1.2 on 2024-11-03 10:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('candleimages', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candleimages',
            name='breakeven_candle',
        ),
        migrations.RemoveField(
            model_name='candleimages',
            name='two_hour_candle',
        ),
    ]