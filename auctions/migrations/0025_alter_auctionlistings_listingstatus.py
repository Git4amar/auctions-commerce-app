# Generated by Django 4.0.5 on 2022-07-02 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0024_alter_auctionlistings_listingstatus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionlistings',
            name='listingStatus',
            field=models.BooleanField(default=True),
        ),
    ]
