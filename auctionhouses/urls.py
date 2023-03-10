from django.contrib import admin
from django.urls import include, path
from auctionhouses import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('details/', views.details, name='details'),
    path('follow/', views.follow, name='follow'),
    path('auctiondetails/', views.auctiondetails, name='auctiondetails'),
    path('search/', views.search, name='search'),
    path('predictivehints/', views.getpredictivehints, name='getpredictivehints'),
    #     AJAX CALL

    path('getFeaturedAuctionHouses/', views.getFeaturedAuctionHouses, name='getFeaturedAuctionHouses'),
    path('getAuctionHouses/', views.getAuctionHouses, name='getAuctionHouses'),
    path('getCurrentAuctionHouse/', views.getCurrentAuctionHouse, name="getCurrentAuctionHouse"),
    # path('getPastAuctionData/', views.getPastAuctionData, name="getPastAuctionData"),
]
