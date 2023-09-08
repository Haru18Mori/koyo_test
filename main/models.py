from django.db import models
from datetime import timedelta
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class Club(models.Model):
    name = models.CharField(verbose_name="部活名")
    image = models.ImageField(verbose_name="活動写真")
    created_at = models.DateTimeField(verbose_name="登録日時",auto_now_add=True)
    introduction = models.CharField(max_length=150,verbose_name="紹介文")
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse()
    
