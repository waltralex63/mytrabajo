from django.db import models
from django.utils import timezone

class Titulo (models.Model):
    titulo = models.CharField(max_length=25)
    def __str__(self):
        return self.titulo

class Empleado(models.Model):

    autor = models.ForeignKey ('auth.User')
    nombre1 = models.CharField(max_length=20)
    nombre2 = models.CharField(max_length=20)
    apellido1 = models.CharField(max_length=20)
    apellido2 = models.CharField(max_length=20)
    fechanaci = models.DateField()
    telefono = models.CharField(max_length=25)
    direccion = models.CharField(max_length=50)
    titulo =   models.ForeignKey(Titulo)
    experiencia = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre2
