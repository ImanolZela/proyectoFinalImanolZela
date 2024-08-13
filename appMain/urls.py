from django.urls import path
from appMain.views import *

urlpatterns = [
    path('', inicio, name = 'main'),
    path('pagina-about/', about, name = 'about'),
    path('pagina-products/', products, name = 'products'),
    path('details/', details, name = 'details'),
]