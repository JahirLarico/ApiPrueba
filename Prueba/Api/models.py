from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    clave = models.CharField(max_length=50, null=True, blank=True)
    nombre = models.CharField(max_length=50, null=True, blank=True)

class Estudiantes(models.Model):
    colegio = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="estudiantes")
    nombreEstudiante = models.CharField(max_length=50)
    apellidoEstudiante = models.CharField(max_length=50)
    edad = models.IntegerField()
    nombreApoderado = models.CharField(max_length=50)
    celularApoderado = models.CharField(max_length=50)
    correoApoderado = models.CharField(max_length=50)

    def __str__(self):
        return self.nombreEstudiante