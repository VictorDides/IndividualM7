from django.db import models

class Etiqueta(models.Model):
    nombre = models.CharField(max_length=50)

class Tarea(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_vencimiento = models.DateTimeField()
    etiquetas = models.ManyToManyField(Etiqueta)
    observaciones = models.TextField(blank=True, null=True)
    completada = models.BooleanField(default=False)