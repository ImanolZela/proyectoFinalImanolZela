from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages

def inicio(request):
    return render(request, 'appMain/index.html')
    
def about(request):
    return render(request, 'appMain/about.html')

@login_required
def createProducts(request):
    usuario = request.user
    
    perfil_configurado = all([
        usuario.perfil.telefono, 
        usuario.perfil.ciudad
    ])

    if request.method == 'POST':
        if not perfil_configurado:
            return render(request, 'appMain/createProducts.html', {'perfil_no_configurado': True})
        else:
            nombre = request.POST['nombre']
            precio = request.POST['precio']
            categoria = request.POST['categoria']
            descripcion = request.POST['descripcion']
            imagen = request.FILES.get('imagen', None)
            producto = Producto(
                nombre=nombre,
                precio=precio,
                categoria=categoria,
                descripcion=descripcion,
                imagen=imagen,
                vendedor=request.user
            )
            producto.save()

            return redirect('products')

    return render(request, 'appMain/createProducts.html')
    
def products(request):
    productos_componentes = Producto.objects.filter(categoria='componentes')
    productos_laptops = Producto.objects.filter(categoria='laptops')
    productos_perifericos = Producto.objects.filter(categoria='perifericos')
    productos_monitores = Producto.objects.filter(categoria='monitores')
    productos_electronica = Producto.objects.filter(categoria='electronica')

    context = {
        'productos_componentes': productos_componentes,
        'productos_laptops': productos_laptops,
        'productos_perifericos': productos_perifericos,
        'productos_monitores': productos_monitores,
        'productos_electronica': productos_electronica,
    }
    return render(request, 'appMain/products.html', context)

class detailsProduct(DetailView):
    model = Producto
    template_name = "appMain/detailsProducts.html"

class updateProducts(LoginRequiredMixin,UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = "appMain/updateProducts.html"
    success_url = reverse_lazy('products')

class deleteProducts(LoginRequiredMixin,DeleteView):
    model = Producto
    success_url = reverse_lazy('products')

class comentProducts(LoginRequiredMixin, CreateView):
    model = Comentario
    template_name = "appMain/detailsProducts.html"
    fields= ['texto']

    def form_valid(self, form):
        producto = Producto.objects.get(pk=self.kwargs['pk'])
        form.instance.producto = producto
        form.instance.usuario = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('details', kwargs={'pk': self.object.producto.pk})
