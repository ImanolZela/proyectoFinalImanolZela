from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    telefono = models.CharField(max_length=15, blank=True)
    ciudad = models.CharField(max_length=100, blank=True)
    imagen_perfil = models.ImageField(upload_to='perfil/', blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} Perfil'
