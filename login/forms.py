from django import forms
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
  password = forms.CharField(
    label="비밀번호를 입력하세요",
    widget=forms.PasswordInput(attrs={'class': 'password-input'}),
  )
  password2 = forms.CharField(
      label="Password confirmation",
      widget=forms.PasswordInput(attrs={'class': 'password-input'}),
  )

  def clean(self):
      cleaned_data = super().clean()
      password1 = cleaned_data.get("password1")
      password2 = cleaned_data.get("password2")

      if password1 and password2 and password1 != password2:
          self.add_error('password2', '비밀번호가 다릅니다.')

      return cleaned_data