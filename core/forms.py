from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
  class Meta:
    model = User
    fields = ('username', 'email', 'password1', 'password2')

  username = forms.CharField(widget=forms.TextInput(attrs={
    'placeholder': 'Your username',
    'class': 'w-100 py-2 px-6 rounded'
  }))
  email = forms.CharField(widget=forms.EmailInput(attrs={
    'placeholder': 'Your email address',
    'class': 'w-100 py-2 px-6 rounded'
  }))
  password1 = forms.CharField(widget=forms.PasswordInput(attrs={
    'placeholder': 'Your password',
    'class': 'w-100 py-2 px-6 rounded'
  }))
  password2 = forms.CharField(widget=forms.PasswordInput(attrs={
    'placeholder': 'Repeat password',
    'class': 'w-100 py-2 px-6 rounded'
  }))