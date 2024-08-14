from django.shortcuts import render
from django.contrib.auth import login, authenticate
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required

def userlogin(request):
    msg_login =" "
    if request.method == 'POST':
        form =AuthenticationFormCustom(request, data=request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contrasena = form.cleaned_data.get('password')

            user = authenticate(username = usuario, password = contrasena)

            if user:
                login(request, user)
                return render(request, 'appMain/index.html')
            
        msg_login = "usuario o contrasena incorrectos" #cambio de mensaje con modal

    form = AuthenticationFormCustom()
    return render(request, 'appCuentas/login.html', {'form': form, 'msg_login': msg_login})
    
def register(request):
    if request.method == 'POST':
        form = userRegisterForm(request.POST)
        if form.is_valid():

            form.save()
            return render(request, 'appMain/index.html')

        #error en datos ingresados con modal

    form = userRegisterForm()
    return render(request, 'appCuentas/register.html', {'form': form})

@login_required
def perfil(request):
    usuario = request.user

    if not hasattr(usuario, 'perfil'):
       Perfil.objects.create(user=usuario)

    if request.method == 'POST':
        form = userUpdateForm(request.POST, request.FILES, instance = usuario)
        if form.is_valid():
            usuario.perfil.telefono = form.cleaned_data.get('telefono')
            usuario.perfil.ciudad = form.cleaned_data.get('ciudad')
            if form.cleaned_data.get('imagen'):
                usuario.perfil.imagen_perfil = form.cleaned_data.get('imagen')
                
            usuario.perfil.save()
            form.save()
            return render(request, 'appMain/index.html' )
    else:
        form = userUpdateForm(instance=usuario)
        
    return render(request, 'appCuentas/perfil.html', {"form": form})
    