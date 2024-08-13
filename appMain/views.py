from django.shortcuts import render
from .forms import ProductoForm

# Create your views here.
def inicio(request):
    return render(request, 'appMain/index.html')
    
def about(request):
    return render(request, 'appMain/about.html')
    
def products(request):

    form = ProductoForm()
    return render(request, 'appMain/products.html', {'form': form})

def details(request):
    return render(request, 'appMain/detailsProducts.html')