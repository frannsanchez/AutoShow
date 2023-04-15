from django.db import models

class Auto(models.Model):
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)
    ano = models.CharField(max_length=4)
    descripcion = models.CharField(max_length=1000)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.marca} - {self.modelo} - {self.ano}"
