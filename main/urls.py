from django.urls import path

from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("club",views.ClubView.as_view(),name="club"),
    path("access",views.AccessView.as_view(),name="access"),
    path("PR_movie",views.MovieView.as_view(),name="PR_movie"),
    path("performance",views.PerformanceView.as_view(),name="performance"),
    path("schedule",views.SceduleView.as_view(), name="schedule"),
    path("guide_map",views.GuideMapView.as_view(),name="guide_map"),
    path("questions",views.QuestionsView.as_view(),name="question"),
    path("announce",views.AnnounceView.as_view(),name="announce"),
]