# Generated by Django 5.1.2 on 2024-10-31 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mgicandles', '0002_mgicandles_delete_candle'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mgicandles',
            options={'verbose_name': 'Mgi Candle', 'verbose_name_plural': 'Mgi Candles'},
        ),
        migrations.RenameField(
            model_name='mgicandles',
            old_name='five_min_break_of_structure',
            new_name='asian_kill_zone',
        ),
        migrations.RenameField(
            model_name='mgicandles',
            old_name='four_hour_break_of_structure',
            new_name='fifteen_min_break_of_structure',
        ),
        migrations.RenameField(
            model_name='mgicandles',
            old_name='pips_lost',
            new_name='pips_stoplost',
        ),
        migrations.RemoveField(
            model_name='mgicandles',
            name='take_profit_candle',
        ),
        migrations.AddField(
            model_name='mgicandles',
            name='fractal_and_alligator',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='mgicandles',
            name='fvg_blocks',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='mgicandles',
            name='london_kill_zone',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='mgicandles',
            name='newyork_kill_zone',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='mgicandles',
            name='previous_day_color_structure',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='mgicandles',
            name='swing_trade_candle',
            field=models.ImageField(blank=True, null=True, upload_to='swing_trade_candle/'),
        ),
        migrations.AddField(
            model_name='mgicandles',
            name='take_profit_one_candle',
            field=models.ImageField(blank=True, null=True, upload_to='take_profit_one_candle/'),
        ),
        migrations.AddField(
            model_name='mgicandles',
            name='take_profit_two_candle',
            field=models.ImageField(blank=True, null=True, upload_to='take_profit_two_candle/'),
        ),
    ]
