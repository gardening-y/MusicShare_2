from django import forms
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
  password = forms.CharField(
    label="비밀번호를 입력하세요",
    widget=forms.PasswordInput(attrs={'class': 'password-input'}),
  )
  password2 = forms.CharField(
    label="비밀번호를 입력하세요",
    widget=forms.PasswordInput(attrs={'class': 'password2-input'}),
  )
