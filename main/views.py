from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.contrib import auth  
from django.db.models import Q
from django.shortcuts import  get_object_or_404,redirect, render  # redirect を追加
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy  
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from .models import Club
# Create your views here.

class IndexView(TemplateView):
    template_name = "main/index.html"

class ClubView(ListView):
    template_name = "main/club.html"
    model = Club
    context_object_name = "clubs"

    def get_queryset(self):
        club = super().get_queryset().order_by('order')
        return club
    
class AccessView(TemplateView):
    template_name = "main/access.html"

class MovieView(TemplateView):
    template_name = "main/movie.html"
    
class MusicView(TemplateView):
    pass

class ScheduleView(TemplateView):
    pass

class MapView(TemplateView):
    pass

class NewsView(TemplateView):
    pass
