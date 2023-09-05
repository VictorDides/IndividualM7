from django.db import models
from django.contrib.auth.models import User

class Etiqueta(models.Model):
    nombre = models.CharField(max_length=50)

class Prioridad(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Tarea(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_vencimiento = models.DateTimeField()
    etiquetas = models.ManyToManyField(Etiqueta)
    observaciones = models.TextField(blank=True, null=True)
    completada = models.BooleanField(default=False)
    asignada_a = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tareas_asignadas', null=True)
    prioridad = models.ForeignKey(Prioridad, on_delete=models.SET_NULL, null=True, blank=True)

