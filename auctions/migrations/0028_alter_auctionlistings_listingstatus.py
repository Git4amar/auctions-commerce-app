# Generated by Django 4.0.5 on 2022-07-02 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0027_remove_auctionlistings_modifydate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionlistings',
            name='listingStatus',
            field=models.CharField(choices=[('active', 'Active'), ('closed', 'Closed')], default='active', max_length=6),
        ),
    ]
