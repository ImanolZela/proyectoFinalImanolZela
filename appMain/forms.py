from django import forms

from django import forms

class ProductoForm(forms.Form):
    nombre = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control custom-input', 'id': 'product-name'}))
    precio = forms.DecimalField(max_digits=10, decimal_places=2, widget=forms.NumberInput(attrs={'class': 'form-control custom-input', 'id': 'product-price'}))
    categoria = forms.ChoiceField(
        choices=[
            ('componentes', 'Componentes'),
            ('laptops', 'Laptops'),
            ('perifericos', 'Periféricos'),
            ('monitores', 'Monitores'),
            ('electronica', 'Electrónica')
        ],widget=forms.Select(attrs={'class': 'form-select custom-input', 'id': 'product-category'}))
    
    descripcion = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control custom-input', 'id': 'product-description', 'rows': 4}))
    imagen = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': 'form-control custom-input', 'id': 'product-image'}))
