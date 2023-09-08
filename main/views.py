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

class ClubView(TemplateView,ListView):
    template_name = "main/club.html"
    model = Club
    fields=["name","image","created_at","introduction"]

    def get_queryset(self):
        clubs = Club.objects.all.order_by('-created_at')
        return clubs

class AccessView(TemplateView):
    template_name = "main/access.html"

class MovieView(TemplateView):
    template_name = "main/movie.html"
    
    
