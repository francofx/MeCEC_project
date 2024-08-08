from django import forms
from .models import Registro

class RegistroForm(forms.ModelForm):
    class Meta:
        model = Registro
        fields = '__all__'
        widgets = {
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'nombres': forms.TextInput(attrs={'class': 'form-control'}),
            'dni': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_nac': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control'}),
            'provincia': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre_apellido_paterno': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre_apellido_materno': forms.TextInput(attrs={'class': 'form-control'}),
            'celular': forms.TextInput(attrs={'class': 'form-control'}),
            'domicilio_actual': forms.TextInput(attrs={'class': 'form-control'}),
            'correo_electronico': forms.EmailInput(attrs={'class': 'form-control'}),
            'foto': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'ministerio': forms.TextInput(attrs={'class': 'form-control'}),
            'registro': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_pabellon': forms.TextInput(attrs={'class': 'form-control'}),
            'numero_pabellon': forms.TextInput(attrs={'class': 'form-control'}),
            'seccion_pabellon': forms.TextInput(attrs={'class': 'form-control'}),
            'otros_pabellon': forms.TextInput(attrs={'class': 'form-control'}),
            'autorizacion_iglesia': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }