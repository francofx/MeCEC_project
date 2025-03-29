from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegistroForm, Registro 
from django.contrib.auth.decorators import login_required
from .models import Registro
from django.urls import reverse



def home(request):
    return render(request, 'home.html')



def formulario(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'home.html')
    else:
        form = RegistroForm()
    return render(request, 'formulario.html', {'form': form})

@login_required
def listado_registros(request):
    query = request.GET.get('q')
    if query:
        registros = Registro.objects.filter(nombres__icontains=query)
    else:
        registros = Registro.objects.all().order_by('ministerio')
        #filtros
        nombre = request.GET.get('nombre')
        apellido = request.GET.get('apellido')
        dni = request.GET.get('dni')
        activo = request.GET.get('activo')

        if nombre:
            registros = registros.filter(nombres__icontains=nombre)
        if apellido:
            registros = registros.filter(apellido__icontains=apellido)
        if dni:
            registros = registros.filter(dni__icontains=dni)
        if activo is not None:
            registros = registros.filter(activo=activo)
        #end filtros
    return render(request, 'listado.html', {'registros': registros})

def registro_detalle(request, id):
    registro = get_object_or_404(Registro, id=id)
    return render(request, 'registro_detalle.html', {'registro': registro})

def control_view(request):
    if request.method == "POST":
        dni = request.POST.get('dni')  # Obtiene el DNI ingresado
        if dni:
            registro = Registro.objects.filter(dni=dni).first()  # Busca el registro por DNI
            if registro:
                return redirect(reverse('registro:registro_detalle', args=[registro.id]))  # Corrige el namespace
    return render(request, 'registro/control.html')

def carnet_view(request, dni):
    registro = get_object_or_404(Registro, dni=dni)  # Buscar por DNI en el modelo Registro
    return render(request, 'registro/carnet.html', {'registro': registro})