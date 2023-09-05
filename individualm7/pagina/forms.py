from django import forms
from .models import Tarea, Etiqueta
from django.contrib.auth.models import User


class FiltroTareasForm(forms.Form):
    etiquetas = forms.ModelMultipleChoiceField(queryset=Etiqueta.objects.all(), required=False)
    completada = forms.BooleanField(required=False)

class TareaForm(forms.ModelForm):
    asignada_a = forms.ModelChoiceField(queryset=User.objects.all(), required=False)

    class Meta:
        model = Tarea
        fields = ['titulo', 'descripcion', 'fecha_vencimiento', 'etiquetas', 'completada', 'prioridad']