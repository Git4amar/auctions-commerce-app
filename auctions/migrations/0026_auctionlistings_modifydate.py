# Generated by Django 4.0.5 on 2022-07-02 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0025_alter_auctionlistings_listingstatus'),
    ]

    operations = [
        migrations.AddField(
            model_name='auctionlistings',
            name='modifyDate',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
