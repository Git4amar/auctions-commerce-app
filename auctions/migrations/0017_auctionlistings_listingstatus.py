# Generated by Django 4.0.5 on 2022-07-02 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0016_alter_auctionlistings_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='auctionlistings',
            name='listingStatus',
            field=models.BooleanField(default=True),
        ),
    ]
