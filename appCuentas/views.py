from django.shortcuts import render, redirect
from django.db import transaction
from django.contrib.auth import login, authenticate
from .forms import *
from .models import *
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView

def userlogin(request):
    error_login = False
    msg_login = ""

    if request.method == 'POST':
        form = AuthenticationFormCustom(request, data=request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contrasena = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contrasena)

            if user is not None:
                login(request, user)
                return render(request, 'appMain/index.html')
            else:
                error_login = True
                msg_login = "Usuario o contraseña incorrectos"
        else:
            error_login = True 
            msg_login = "Usuario o contraseña incorrectos"

    else:
        form = AuthenticationFormCustom()

    return render(request, 'appCuentas/login.html', {'form': form, 'error_login': error_login, 'msg_login': msg_login})

def register(request):
    error_en_formulario = False 

    if request.method == 'POST':
        form = userRegisterForm(request.POST)
        if form.is_valid():
            with transaction.atomic():  
                user = form.save()

                Perfil.objects.create(user=user)

                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                if user is not None:
                    login(request, user)
                    return render(request, 'appMain/index.html')
        else:
            error_en_formulario = True

    else:
        form = userRegisterForm()

    return render(request, 'appCuentas/register.html', {'form': form, 'error_en_formulario': error_en_formulario})

@login_required
def perfil(request):
    usuario = request.user

    if not hasattr(usuario, 'perfil'):
       Perfil.objects.create(user=usuario)

    info_guardada = False

    if request.method == 'POST':
        form = userUpdateForm(request.POST, request.FILES, instance = usuario)
        if form.is_valid():
            usuario.perfil.telefono = form.cleaned_data.get('telefono')
            usuario.perfil.ciudad = form.cleaned_data.get('ciudad')
            if form.cleaned_data.get('imagen'):
                usuario.perfil.imagen_perfil = form.cleaned_data.get('imagen')
                
            usuario.perfil.save()
            form.save()
            info_guardada = True
    else:
        form = userUpdateForm(instance=usuario, initial={'telefono':usuario.perfil.telefono, 'ciudad': usuario.perfil.ciudad})
        
    return render(request, 'appCuentas/perfil.html', {"form": form, "info_guardada": info_guardada} )

class updatePassword(LoginRequiredMixin, PasswordChangeView):
    form_class = CustomPasswordChangeForm
    template_name = 'appCuentas/updatePassword.html'
    success_url = reverse_lazy('perfil')

    def form_valid(self, form):
        super().form_valid(form)
        return render(self.request, self.template_name, {
            'form': form,
            'password_updated': True
        })