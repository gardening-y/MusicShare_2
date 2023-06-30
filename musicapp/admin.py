from django.contrib import admin
from .models import Music

# Register your models here.

class MusicAdmin(admin.ModelAdmin):
  list_display = ['title', 'content', 'author', 
    'datetime', 'music_title', 'music_singer']

admin.site.register(Music, MusicAdmin)
