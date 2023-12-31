from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("closed", views.closed, name="closed"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.createListing, name="createListing"),
    path("listing/<str:listingID>", views.listing, name="listing"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("categories/<str:category>", views.categories, name="categories")
]
