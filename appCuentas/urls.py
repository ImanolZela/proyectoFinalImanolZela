from django.urls import path
from appCuentas.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('pagina-login/', userlogin, name = 'login'),
    path('pagina-register/', register, name = 'register'),
    path('pagina-perfil/', perfil, name = 'perfil'),
    path('logout/', LogoutView.as_view(template_name="appMain/index.html"), name='logout'), 
] 