# Generated by Django 4.0.5 on 2022-07-03 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0030_rename_auctionlisting_comments_listing_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='comment',
            field=models.TextField(verbose_name='Comment on Listing'),
        ),
    ]
