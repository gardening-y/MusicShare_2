from django.db import models

# Create your models here.
class Music(models.Model):
  title=models.CharField(max_length=20)
  content=models.TextField(null=True)
  author=models.CharField(max_length=20)
  datetime=models.DateTimeField(auto_now=True)
  music_title=models.CharField(max_length=20,null=True)
  music_singer=models.CharField(max_length=20,null=True)
  image=models.ImageField(null=True, blank=True)
  
  def __str__(self):
    return self.title
