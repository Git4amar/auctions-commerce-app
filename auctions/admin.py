from django.contrib import admin
from .models import *

class ListingsAdmin(admin.ModelAdmin):
    list_display = ("title", "startingBid", "listingMaxBid")

class BidAdmin(admin.ModelAdmin):
    list_display = ("listing", "bid")

class CommentAdmin(admin.ModelAdmin):
    list_display = ("listing", "comment")

# Register your models here.
admin.site.register(auctionListings, ListingsAdmin)
admin.site.register(bids, BidAdmin)
admin.site.register(comments, CommentAdmin)