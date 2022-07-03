from dataclasses import fields
from django.forms import BooleanField, CheckboxInput, ModelForm, NumberInput, TextInput, Textarea, URLInput

from .models import auctionListings, bids, comments

# createListingForm = modelform_factory(auctionListings, exclude=("createdByUser", "createDate", "usersWatching"))
class createListingForm(ModelForm):
    class Meta:
        model = auctionListings
        exclude = ["createdByUser", "createDate", "usersWatching", "listingMaxBid", "listingStatus"]
        widgets = {
            'title' : TextInput(attrs={'class' : 'form-control mb-2 ms-2', 'autofocus' : 'autofocus'}),
            'description' : Textarea(attrs={'class' : 'form-control mb-2 ms-2', 'rows' : 5}),
            'startingBid' : NumberInput(attrs={'min' : 0, 'class' : 'form-control mb-2 ms-2'}),
            'imageURL' : URLInput(attrs={'class' : 'form-control mb-2 ms-2'}),
            'category' : TextInput(attrs={'class' : 'form-control mb-2 ms-2'})
        }

class placeBidForm(ModelForm):
    class Meta:
        model = bids
        fields = ['bid']
        widgets = {
            'bid' : NumberInput(attrs={'min' : 0, 'class' : 'form-control mb-2', 'placeholder' : 'Bid','autofocus' : 'autofocus'})
        }

class listingStatusForm(ModelForm):
    listingStatus = BooleanField(
        required = False,
        widget = CheckboxInput(attrs={'class' : 'form-check-input', 'role' : 'switch', 'onchange':'this.form.submit()'})
    )
    class Meta:
        model = auctionListings
        fields = ['listingStatus']

class commentForm(ModelForm):
    class Meta:
        model = comments
        fields = ['comment']
        widgets = {
            'comment' : Textarea(attrs={'class' : 'form-control mb-2 ms-2', 'rows' : 3, 'placeholder' : 'Comment on Listing'})
        }