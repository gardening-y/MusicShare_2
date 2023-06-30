from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

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
    
    
def login_view(request):
  if request.method == 'GET':
    return render(request, 'login/login.html', {'form': AuthenticationForm()})
  
  else:
    form = AuthenticationForm(request, data=request.POST)
    if form.is_valid():
      login(request, form.user_cache)
      return redirect('index')
    else:
      return render(request, 'login/login.html', {'form': form})

def logout_view(request):
  if request.user.is_authenticated:
    logout(request)
  return redirect('index')