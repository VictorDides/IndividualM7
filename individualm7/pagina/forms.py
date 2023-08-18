from django import forms
from .models import Tarea, Etiqueta

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['titulo', 'descripcion', 'fecha_vencimiento', 'etiquetas']


class FiltroTareasForm(forms.Form):
    etiquetas = forms.ModelMultipleChoiceField(queryset=Etiqueta.objects.all(), required=False)
    completada = forms.BooleanField(required=False)