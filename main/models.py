from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class Club(models.Model):
    name = models.CharField(verbose_name="部活名",max_length=20)
    image = models.ImageField(verbose_name="活動写真", upload_to="images/")
    order = models.FloatField(verbose_name="優先順位",default=0)
    introduction = models.CharField(max_length=150,verbose_name="紹介文")
    question = models.TextField(max_length=300,verbose_name="アンケート",default="部長にアンケートを行いました!")
    question1 = models.TextField(max_length=300,verbose_name="①今回の音展での出し物で特にこれといった推しがあれば教えてください",default="①今回の音展での出し物で特にこれといった推しがあれば教えてください")
    question2 = models.TextField(max_length=300,verbose_name="②部長の趣味を教えてください",default="②部長の趣味を教えてください")
    question3 = models.TextField(max_length=300,verbose_name="③なぜこの部活に参加しようと思ったのですか?",default="③なぜこの部活に参加しようと思ったのですか?")
    question4 = models.TextField(max_length=300,verbose_name="④部活動の中で一番やりがいを感じていることはどう言うことですか?",default="④部活動の中で一番やりがいを感じていることはどう言うことですか?")





    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse()

class Photo(models.Model):
    name = models.CharField(verbose_name="場所",max_length=20)  
    image = models.ImageField(verbose_name="写真", upload_to="images/")
    order = models.FloatField(verbose_name="優先順位",default=0)