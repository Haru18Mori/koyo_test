from django.urls import path

from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="home"),
    path("club",views.ClubView.as_view(),name="club"),
    path("access",views.AccessView.as_view(),name="access"),
    path("music",views.MusicView.as_view(),name="music"),
    path("schedule",views.ScheduleView.as_view(), name="schedule"),
    path("map",views.MapView.as_view(),name="map"),
    path("news",views.NewsView.as_view(),name="news"),
]