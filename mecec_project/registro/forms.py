from django import forms
from .models import Registro

class RegistroForm(forms.ModelForm):
    fecha_nac = forms.DateField(
        input_formats=['%d/%m/%Y'],  # Ejemplo de formato DD/MM/YYYY
        widget=forms.DateInput(attrs={
            'placeholder': 'DD/MM/YYYY',
            'class': 'form-control'
        })
    )
    class Meta:
        model = Registro
        fields = '__all__'
