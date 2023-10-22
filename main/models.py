from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class Club(models.Model):
    name = models.CharField(verbose_name="部活名",max_length=20)
    image = models.ImageField(verbose_name="活動写真", upload_to="images/")
    order = models.FloatField(verbose_name="優先順位",default=0)
    introduction = models.CharField(max_length=150,verbose_name="紹介文")
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse()

class Photo(models.Model):
    name = models.CharField(verbose_name="場所",max_length=20)  
    image = models.ImageField(verbose_name="写真", upload_to="images/")
    order = models.FloatField(verbose_name="優先順位",default=0)