# Generated by Django 4.0.5 on 2022-07-02 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0015_alter_auctionlistings_listingmaxbid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionlistings',
            name='category',
            field=models.CharField(blank=True, default='No Category Listed', max_length=64, verbose_name='Category'),
        ),
    ]
