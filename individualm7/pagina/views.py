from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import Tarea
from .forms import TareaForm 

# Create your views here.
def landing(request):
    return render(request,'pagina/landing.html')

def listar_tareas(request):
    tareas = Tarea.objects.filter().order_by('fecha_vencimiento')
    return render(request, 'pagina/listar_tareas.html', {'tareas': tareas})

def ver_tarea(request, tarea_id):
    tarea = get_object_or_404(Tarea, pk=tarea_id)
    return render(request, 'pagina/ver_tarea.html', {'tarea': tarea})

def crear_tarea(request):
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_tareas')
    else:
        form = TareaForm()
    
    return render(request, 'pagina/crear_tarea.html', {'form': form})


def editar_tarea(request, tarea_id):
    tarea = get_object_or_404(Tarea, pk=tarea_id)
    
    if request.method == 'POST':
        form = TareaForm(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
            return redirect('pagina/ver_tarea', tarea_id=tarea.id)  
    else:
        form = TareaForm(instance=tarea)
    
    return render(request, 'pagina/editar_tarea.html', {'form': form, 'tarea': tarea})

def eliminar_tarea(request, tarea_id):
    tarea = get_object_or_404(Tarea, pk=tarea_id)
    
    if request.method == 'POST':
        tarea.delete()
        return redirect('listar_tareas')  
    
    return render(request, 'pagina/eliminar_tarea.html', {'tarea': tarea})
