from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
  username = forms.CharField(widget=forms.TextInput(attrs={
    'placeholder': 'Ваш логин',
    'class': 'form-control'
  }))
  password = forms.CharField(widget=forms.PasswordInput(attrs={
    'placeholder': 'Ваш пароль',
    'class': 'form-control'
  }))

class SignUpForm(UserCreationForm):
  class Meta:
    model = User
    fields = ('username', 'email', 'password1', 'password2')

  username = forms.CharField(widget=forms.TextInput(attrs={
    'placeholder': 'Ваш логин',
    'class': 'form-control'
  }))
  email = forms.CharField(widget=forms.EmailInput(attrs={
    'placeholder': 'Ваша почта',
    'class': 'form-control'
  }))
  password1 = forms.CharField(widget=forms.PasswordInput(attrs={
    'placeholder': 'Ваш пароль',
    'class': 'form-control'
  }))
  password2 = forms.CharField(widget=forms.PasswordInput(attrs={
    'placeholder': 'Повторите пароль',
    'class': 'form-control'
  }))