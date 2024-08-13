from django.shortcuts import render
from django.contrib.auth import login, authenticate
from .forms import *
    
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

def perfil(request):
    return render(request, 'appCuentas/perfil.html')
    