from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.conf import settings
from django.views.generic import RedirectView
from adminsite import views

urlpatterns = [
    path('galleries/', views.galleries, name='galleries'),
    path('gevents/', views.gevents, name='gevents'),
    path('artists/', views.artists, name='artists'),
    path('artworks/', views.artworks, name='artworks'),
    path('museums/', views.museums, name='museums'),
    path('mevents/', views.mevents, name='mevents'),
    path('museumpieces/', views.museumpieces, name='museumpieces'),
    path('auctionhouses/', views.auctionhouses, name='auctionhouses'),
    path('auctions/', views.auctions, name='auctions'),
    path('lots/', views.lots, name='lots'),
    path('getevents/', views.getevents, name='getevents'),
    path('searchgallery/', views.searchgalleries, name='searchgalleries'),
    path('editgallery/', views.editgallery, name='editgallery'),
    path('savegallery/', views.savegallery, name='savegallery'),
    path('searchgevents/', views.searchgevents, name='searchgevents'),
    path('editgevent/', views.editgevent, name='editgevent'),
    path('savegevent/', views.savegevent, name='savegevent'),
    path('searchartworks/', views.searchartworks, name='searchartworks'),
    path('editartwork/', views.editartwork, name='editartwork'),
    path('saveartwork/', views.saveartwork, name='saveartwork'),
]


