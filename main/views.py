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
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from .models import Club,Photo
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
    
class ClubDetailView(DetailView):
    model = Club
    template_name = "main/club__detail.html"
    context_object_name = "club"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # 親クラスのメソッドを呼び出してコンテキストを取得
        
        data_list = Club.objects.filter(id=self.kwargs["pk"])  # データをフィルタリングして取得
        context["club_data_list"] = data_list  # コンテキストにデータを追加
        
        return context  # 最終的なコンテキストを返す

    
    
    # def post(self, request, **kwargs):
    #     print(self.kwargs["pk"]) # ←このような形で取得可能

    #     # 詳細画面へ遷移させる
    #     return redirect('club__detail', pk=self.kwargs["pk"])
    
    
class AccessView(TemplateView):
    template_name = "main/access.html"

    
class MusicView(TemplateView):
    template_name = "main/music.html"

class GalleryView(ListView):
    template_name = "main/gallery.html"
    model = Photo
    context_object_name = "photos"

    def get_queryset(self):
        photo = super().get_queryset().order_by('order')
        return photo

class MapView(TemplateView):
    template_name = "main/map.html"

class NewsView(TemplateView):
    template_name = "main/news.html"

# class SpaceView(TemplateView):
#     template_name = "main/space.html"