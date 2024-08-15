from django.db import models
from django.contrib.auth.models import User

class Producto(models.Model):
    SECCION_OPCIONES = [
        ('componentes', 'Componentes'),
        ('laptops', 'Laptops'),
        ('perifericos', 'Periféricos'),
        ('monitores', 'Monitores'),
        ('electronica', 'Electrónica'),
    ]
    
    vendedor = models.ForeignKey(User, on_delete=models.CASCADE,)
    nombre = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.CharField(max_length=50, choices=SECCION_OPCIONES)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='productos/')

    def __str__(self):
        return self.nombre

class Comentario(models.Model):
    producto = models.ForeignKey(Producto, related_name='comentarios', on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comentario de {self.usuario.username} en {self.producto.nombre}'