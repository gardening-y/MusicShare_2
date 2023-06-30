from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import SignUpForm

from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def signup(request):
  if request.method == 'GET':
    form = SignUpForm
    context = {'form' : form}
    return render(request, 'login/signup.html', context)
  
  else:
    form = SignUpForm(request.POST)
    
    if form.is_valid():
      instance = form.save()
      return redirect('index')
    else:
      return redirect('login:signup')
    
def login(request):
  #GET, POST 분리
  if request.method == 'GET':
    # 로그인 HTML 응답
    pass
  
  else:
    pass
    # 데이터 유효성 검사
    # 비즈니스 로직 처리
    # 응답
