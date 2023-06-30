from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.
def signup(request):
  if request.method == 'GET':
    form = UserCreationForm
    context = {'form' : form}
    return render(request, 'login/signup.html', context)
  
  else:
    form = UserCreationForm(request.POST)
    
    if form.is_valid():
      instance = form.save()
      return redirect('index')
    else:
      return redirect('login:signup')
    
def login(request):
  if request.method == 'GET':
    pass
  
  else:

    form = AuthenticationForm(request.POST)
    if form.is_valid():
      pass
    else:
      pass
