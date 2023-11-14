# Generated by Django 4.0.5 on 2022-07-02 00:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0013_rename_auctionlisting_bids_listing_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='auctionlistings',
            name='listingMaxBid',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=19, validators=[django.core.validators.MinValueValidator(limit_value=0)], verbose_name='Current Bid'),
            preserve_default=False,
        ),
    ]
