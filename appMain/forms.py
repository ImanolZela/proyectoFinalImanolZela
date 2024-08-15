from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    nombre = forms.CharField(required=True, max_length=200, widget=forms.TextInput(attrs={'class': 'form-control custom-input', 'id': 'nombre'}))
    precio = forms.DecimalField(required=True, max_digits=10, decimal_places=2, widget=forms.NumberInput(attrs={'class': 'form-control custom-input', 'id': 'precio'}))
    categoria = forms.ChoiceField(choices=Producto.SECCION_OPCIONES,widget=forms.Select(attrs={'class': 'form-control custom-input', 'id': 'categoria'}))
    descripcion = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form-control custom-input', 'id': 'descripcion', 'rows': 4}))
    imagen = forms.ImageField(required=False, widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))

    class Meta:
       model = Producto
       fields = ['nombre', 'precio', 'categoria', 'descripcion', 'imagen']
       