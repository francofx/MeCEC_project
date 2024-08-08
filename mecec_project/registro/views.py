from django.shortcuts import render, redirect
from .forms import RegistroForm, Registro 

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

def listado_registros(request):
    query = request.GET.get('q')
    if query:
        registros = Registro.objects.filter(nombres__icontains=query)
    else:
        registros = Registro.objects.all()
    return render(request, 'listado.html', {'registros': registros})

