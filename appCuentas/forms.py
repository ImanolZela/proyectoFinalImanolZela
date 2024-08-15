from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm

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

class userUpdateForm(UserChangeForm):
    password = None
    username = forms.CharField(required=False, max_length=150, widget=forms.TextInput(attrs={'class': 'form-control custom-input', 'id': 'username'}))
    email = forms.EmailField(required=False, widget=forms.EmailInput(attrs={'class': 'form-control custom-input', 'id': 'email'}))
    telefono = forms.CharField(required=False, max_length=15, widget=forms.TextInput(attrs={'class': 'form-control custom-input', 'id': 'telefono'}))
    ciudad = forms.CharField(required=False, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control custom-input', 'id': 'ciudad'}))
    imagen = forms.ImageField(required=False, widget=forms.ClearableFileInput(attrs={'class': 'form-control', 'id': 'imagen'}))

    class Meta:
        model = User
        fields = ['username', 'email','telefono', 'ciudad', 'imagen']

class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label="Contraseña Actual",widget=forms.PasswordInput(attrs={'class': 'form-control','id': 'id_old_password','required': 'required',}))
    new_password1 = forms.CharField(label="Nueva Contraseña",widget=forms.PasswordInput(attrs={'class': 'form-control','id': 'id_new_password1','required': 'required',}) )
    new_password2 = forms.CharField(label="Confirmar Nueva Contraseña",widget=forms.PasswordInput(attrs={'class': 'form-control','id': 'id_new_password2','required': 'required',}))