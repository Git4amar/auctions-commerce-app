# Generated by Django 4.0.5 on 2022-07-04 04:12

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0033_alter_auctionlistings_listingmaxbid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionlistings',
            name='description',
            field=models.TextField(blank=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='auctionlistings',
            name='usersWatching',
            field=models.ManyToManyField(blank=True, related_name='userWatch', to=settings.AUTH_USER_MODEL),
        ),
    ]
