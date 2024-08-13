from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class AuthenticationFormCustom(AuthenticationForm):
     username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control custom-input','placeholder': 'Usuario','id': 'username'}))
     password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control custom-input','placeholder': 'Contraseña','id': 'password'}))

class userRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'form-control custom-input'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control custom-input'}))
    password1 = forms.CharField(label='Contraseña',widget=forms.PasswordInput(attrs={'class': 'form-control custom-input'}))
    password2 = forms.CharField(label='Confirmar Contraseña',widget=forms.PasswordInput(attrs={'class': 'form-control custom-input'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        help_text = {k: "" for k in fields}