from django.shortcuts import render
from django.http import HttpResponse
from .forms import SignUpForm

from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def signup_view(request):
  
  #GET 요청 시 HTML 응답
  if request.method == 'GET':
    form = SignUpForm
    context = {'form' : form}
    return render(request, 'login/signup.html', context)
  
  # POST 요청 시 데이터 확인 후 회원 생성
  else:
    form = SignUpForm(request.POST)
    
    if form.is_valid():
      # 회원가입 처리
      instance = form.save()
      return redirect('login:signup')
    else:
      # redirect 처리
      return redirect('login:signup')
