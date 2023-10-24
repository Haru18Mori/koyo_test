from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="home"),
    path("club",views.ClubView.as_view(),name="club"),
    path("club__detail/<int:pk>", views.ClubDetailView.as_view(), name="club__detail"),
    path("access",views.AccessView.as_view(),name="access"),
    path("music",views.MusicView.as_view(),name="music"),
    path("map",views.MapView.as_view(),name="map"),
    path("news",views.NewsView.as_view(),name="news"),
    path("gallery",views.GalleryView.as_view(),name="gallery"),
    # path("space", views.SpaceView.as_view(),name="space"),
]   


