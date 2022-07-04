from tabnanny import verbose
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinValueValidator
from .templatetags import customFilters


class User(AbstractUser):
    pass

    class Meta:
        verbose_name_plural = 'Users'

    def __str__(self):
        return f"Username: {self.username}, Email: {self.email}, Password: {self.password}"

class auctionListings(models.Model):
    title = models.CharField(max_length=64, verbose_name="Title")
    description = models.TextField(verbose_name="Description", blank=True)
    startingBid = models.DecimalField(max_digits=19, decimal_places=2, validators=[MinValueValidator(limit_value=0)], verbose_name="Starting Bid")
    imageURL = models.URLField(blank=True, verbose_name="Image URL")
    category = models.CharField(max_length=64, blank=True, verbose_name="Category", default="No Category Listed")
    createdByUser = models.ForeignKey(User, on_delete=models.CASCADE, related_name="userAuctionListings")
    createDate = models.DateTimeField(auto_now_add=True)
    usersWatching = models.ManyToManyField(User, related_name="userWatch", blank=True)
    listingMaxBid = models.DecimalField(max_digits=19, decimal_places=2, validators=[MinValueValidator(limit_value=0)], verbose_name="Current Bid", null=True, blank=True)
    listingStatus = models.BooleanField(default=True)

    def __str__(self):
        startBid = customFilters.USD(self.startingBid)
        if self.listingMaxBid:
            maxBid = customFilters.USD(self.listingMaxBid)
        else:
            maxBid = 0
        return f"{self.title} has starting bid of {startBid} and latest bid of {maxBid}"

    class Meta:
        verbose_name_plural = 'Auction Listings'    
    
class bids(models.Model):
    bid = models.DecimalField(max_digits=19, decimal_places=2, validators=[MinValueValidator(limit_value=0)])
    listing = models.ForeignKey(auctionListings, on_delete=models.CASCADE, related_name="listingBids")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="userBids")
    bidDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        bidPrice = customFilters.USD(self.bid)
        username = self.user.username
        auctionTitle = self.listing.title
        return f"Bid of {bidPrice} was place on {auctionTitle} by {username} on {self.bidDate}"

    class Meta:
        verbose_name_plural = 'Bids'

class comments(models.Model):
    comment = models.TextField(verbose_name="Comment on Listing")
    listing = models.ForeignKey(auctionListings, on_delete=models.CASCADE, related_name="listingComments")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="userComments")
    commentDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        username =  self.user.username
        auctionTitle = self.listing.title
        return f"{username}'s comment on {auctionTitle} last modified {self.commentDate}"

    class Meta:
        verbose_name_plural = 'Comments'