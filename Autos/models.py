from django.db import models
from django.contrib.auth.models import User

class Auto(models.Model):
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)
    año = models.CharField(max_length=4)
    color = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=1000)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    dueño = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="dueño")
    imagen = models.ImageField(upload_to="publicaciones", null=True, blank=True)

    def __str__(self):
        return f"{self.marca} - {self.modelo} - {self.año}"

class Profile(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name="profile")
    imagen = models.ImageField(upload_to="perfiles", null=True, blank=True)
    nacionalidad = models.CharField(max_length=20)
    instagram = models.CharField(max_length=50)

class Mensaje(models.Model):
    mensaje = models.TextField(max_length=1000)
    email = models.EmailField()
    destinatario = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="destinatario")