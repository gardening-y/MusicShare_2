from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import  UserCreationForm,AuthenticationForm
from django.forms import ModelForm, TextInput, EmailInput, NumberInput,PasswordInput

class BaseLoginForm(AuthenticationForm):
    class Meta:
        model=get_user_model()
        fields='__all__'

class LoginForm(BaseLoginForm):
    username = forms.CharField(
        max_length=10,
        widget=forms.TextInput(attrs={
            'class': 'box1',
            'style': 'max-width: 300px;',
            'placeholder': '10자 이내로 입력하세요'
        })
    )
    password = forms.CharField(
        max_length=10,
        widget=forms.TextInput(attrs={
            'class': 'box1',
            'style': 'max-width: 300px;',
            'placeholder': '10자 이내로 입력하세요'
        })
    )
    class Meta:
        fields=['username','password']

class UserBaseForm(forms.ModelForm):
    class Meta:
        model=get_user_model()
        fields='__all__'


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        max_length=10,
        widget=forms.TextInput(attrs={
            'class': 'box1',
            'style': 'max-width: 300px;',
            'placeholder': '10자 이내로 입력하세요'
        })
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'box1',
            'style': 'max-width: 300px;',
            'placeholder': '10자 이내로 입력하세요'
        })
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'box1',
            'style': 'max-width: 300px;',
            'placeholder': '10자 이내로 입력하세요'
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'box1',
            'style': 'max-width: 300px;',
            'placeholder': '이메일 입력'
        })
    )
    check = forms.BooleanField(
        label='약관에 동의합니다.',
        required=True,
        widget=forms.CheckboxInput(attrs={'class': 'chk'})
    )

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ['username', 'password1', 'email', 'password2', 'check']
