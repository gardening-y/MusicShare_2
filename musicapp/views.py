from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Music
from django import forms
from django.http import HttpResponse


def index(request):
  writings=Music.objects.all().order_by('-id')
  return render(request, 'musicapp/index.html', {'writings':writings})

@login_required
def create(request):
  if request.method=="GET":
    return render(request, 'musicapp/create.html')
  else:
    Music.objects.create(
      image = request.FILES.get("image"),
      title=request.POST.get('title'),
      content=request.POST.get('content'),
      music_title=request.POST.get('music_title'),
      music_singer=request.POST.get('music_singer'),
      author=request.user
    )
    return redirect('index')
    
def update(request, id):
  writing=get_object_or_404(Music, pk=id)
  if request.method=="GET":
    return render(request, 'musicapp/update.html', {'writing':writing})
  else:
    writing.title=request.POST.get('title')
    writing.content=request.POST.get('content')
    new_image=request.FILES.get('image')
    if new_image:
      writing.image.delete()
      writing.image=new_image
    writing.save()
    return redirect('index')
    
def delete(request, id):
  writing=get_object_or_404(Music, pk=id)
  writing.delete()
  return redirect('mypage',writing.author) 

@login_required
def mypage(request, author):
  try:
    writings = Music.objects.filter(author=author).order_by('-id')
  except Music.DoesNotExist:
    writings = []
  return render(request, 'musicapp/mypage.html', {'writings': writings})



def signup(request):
    if request.method == "POST":
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        res_data={}
        
        if password1 != password2:
            res_data['error'] = '비밀번호가 다릅니다.'
        return render(request, 'signup.html', res_data)
