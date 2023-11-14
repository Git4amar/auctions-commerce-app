from django.contrib.auth import authenticate, login, logout, get_user
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import F
from .models import User, auctionListings, comments
from .forms import createListingForm, placeBidForm, listingStatusForm, commentForm


def index(request):
    listings = auctionListings.objects.all().order_by(F('createDate').desc())
    return render(request, "auctions/index.html", {
        'listings' : listings
    })

def closed(request):
    listings = auctionListings.objects.all().order_by(F('createDate').desc())
    return render(request, "auctions/closedListings.html", {
        'listings' : listings
    })

@login_required
def watchlist(request):
    return render(request, "auctions/watchlist.html")

def categories(request, category):
    if category == "list":
        categories = auctionListings.objects.values('category').order_by('category').distinct()
        return render(request, "auctions/categories.html", {
            "categories": categories
        })
    else:
        listings = auctionListings.objects.filter(category__iexact=category).order_by(F('createDate').desc())
        return render(request, "auctions/category.html", {
            "listings": listings, "category": category
        })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            messages.error(request, 'Invalid username and/or password.')
            return render(request, "auctions/login.html")
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            messages.error(request, 'Passwords must match.')
            return render(request, "auctions/register.html")

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            messages.error(request, 'Username already taken.')
            return render(request, "auctions/register.html")
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


@login_required
def createListing(request):
    if request.method == "GET":
        return render(request, "auctions/createListing.html", {
            "form": createListingForm(initial={'category': None})
        })
    else:
        createForm = createListingForm(request.POST)
        print(createForm.is_valid())
        if createForm.is_valid():
            newListing = createForm.save(commit=False)
            newListing.title = newListing.title.title()
            newListing.createdByUser = get_user(request)
            if newListing.category:
                newListing.category = newListing.category.capitalize()
            newListing.save()
            messages.success(request, 'Listing created successfully')
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/createListing.html", {
            "form": createForm
        })

def listing(request, listingID):
    listing = auctionListings.objects.get(pk=listingID)
    user = get_user(request)
    allComments = comments.objects.filter(listing=listing).order_by(F('commentDate').desc())
    bidForm = placeBidForm(auto_id=False)
    statusForm = listingStatusForm(initial={'listingStatus': listing.listingStatus}, auto_id=False)
    formComment = commentForm(auto_id=False)
    if request.method == "GET":
        return render(request, "auctions/listing.html", {
            "listing": listing, "bidForm": bidForm, "statusForm": statusForm, "commentForm": formComment, "comments": allComments
        })
    else:
        if not user.is_authenticated:
            return HttpResponseRedirect(reverse("login"))
        else:
            # execute watchlist actions if any
            if request.POST.get('watchlist'):
                if request.POST.get('watchlist') == "addWatch":
                    user.userWatch.add(listing)
                    messages.info(request, 'Successfully added to Watchlist')
                elif request.POST.get('watchlist') == "removeWatch":
                    user.userWatch.remove(listing)
                    messages.info(request, 'Successfully removed from Watchlist')
                return HttpResponseRedirect(reverse("listing", kwargs={'listingID' : listing.id}))
            
            # execute bidding actions if any
            if request.POST.get('placeBid'):
                userNewBid = float(request.POST.get('bid'))
                if listing.listingMaxBid:
                    if not userNewBid > listing.listingMaxBid:
                        messages.error(request, 'Bid unsuccessful')
                        return render(request, "auctions/error.html", {
                            "message": "Bid must greater than current price", "code": "406"
                        })
                else:
                    if userNewBid < listing.startingBid:
                        messages.error(request, 'Bid unsuccessful')
                        return render(request, "auctions/error.html", {
                            "message": "Bid must be at least starting bid", "code": "406"
                        })

                newBid = placeBidForm(request.POST).save(commit=False)
                newBid.user = user
                newBid.listing = listing
                newBid.save()
                listing.listingMaxBid = userNewBid
                listing.save()
                messages.success(request, 'Bid placed successfully')
                return HttpResponseRedirect(reverse("listing", kwargs={'listingID' : listing.id}))
            
            # execute and save comments
            if request.POST.get('comment'):
                newComment = commentForm(request.POST).save(commit=False)
                newComment.listing = listing
                newComment.user = user
                newComment.save()
                messages.success(request, 'Comment Success')
                return HttpResponseRedirect(reverse("listing", kwargs={'listingID' : listing.id}))

            # execute Listing Status Action
            if request.POST.get("listingStatus") == "on":
                status = listingStatusForm(request.POST, instance=listing)
                status.save()
                messages.success(request, 'Listing is now active')
            else:
                status = listingStatusForm(request.POST, instance=listing)
                status.save()
                messages.success(request, 'Listing is now closed')
            return HttpResponseRedirect(reverse("listing", kwargs={'listingID' : listing.id}))        