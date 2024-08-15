from django.urls import path
from appMain.views import *

urlpatterns = [
    path('', inicio, name = 'main'),
    path('pagina-about/', about, name = 'about'),
    path('crear-producto/', createProducts ,name='createProducts'),    
    path('pagina-products/', products , name='products'),
    path('details/<pk>/', detailsProduct.as_view(), name = 'details'),
    path('actualizar-producto/<pk>/', updateProducts.as_view(), name = 'updateProducts'),
    path('borrar-producto/<pk>/', deleteProducts.as_view(), name = 'deleteProducts'),
    path('producto/<pk>/comentar/', comentProducts.as_view(), name='comentar'),

]