
from django.contrib import admin
from .models import Registro

@admin.register(Registro)
class RegistroAdmin(admin.ModelAdmin):
    list_display = ('apellido', 'nombres', 'dni', 'ciudad', 'provincia')  # Añade aquí los campos que quieras mostrar en la lista
    search_fields = ('nombres', 'apellido')  # Campos en los que puedes buscar en el panel de administración
