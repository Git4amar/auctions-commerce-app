# Generated by Django 4.0.5 on 2022-07-02 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0028_alter_auctionlistings_listingstatus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionlistings',
            name='listingStatus',
            field=models.BooleanField(default=True),
        ),
    ]
