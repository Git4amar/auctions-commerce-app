# Generated by Django 4.0.5 on 2022-07-01 02:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0012_alter_auctionlistings_startingbid_alter_bids_bid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bids',
            old_name='auctionListing',
            new_name='listing',
        ),
        migrations.RenameField(
            model_name='bids',
            old_name='userId',
            new_name='user',
        ),
    ]
