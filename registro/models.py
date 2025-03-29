from django.db import models

class Registro(models.Model):
    id = models.AutoField(primary_key=True)  # Este es el campo id
    apellido = models.CharField(max_length=100, blank=False, null=False)
    nombres = models.CharField(max_length=100, blank=False, null=False)
    dni = models.CharField(max_length=20, blank=False, null=False)
    fecha_nac = models.DateField()
    ciudad = models.CharField(max_length=100, blank=False, null=False)
    provincia = models.CharField(max_length=100, blank=False, null=False)
    nombre_apellido_paterno = models.CharField(max_length=100)
    nombre_apellido_materno = models.CharField(max_length=100)
    celular = models.CharField(max_length=20, blank=False, null=False)
    domicilio_actual = models.CharField(max_length=255, blank=False, null=False)
    correo_electronico = models.EmailField()
    foto = models.ImageField(upload_to='static/fotos/')
    ministerio = models.CharField(max_length=100, blank=False, null=False)
    registro = models.CharField(max_length=100, blank=False, null=False)
    unidad_carcelaria = models.CharField(max_length=100, blank=False, null=False)
    tipo_pabellon = models.CharField(max_length=100, blank=False, null=False)
    numero_pabellon = models.CharField(max_length=100, blank=False, null=False)
    seccion_pabellon = models.CharField(max_length=100, blank=False, null=False)
    otros_pabellon = models.CharField(max_length=255, blank=True, null=True)
    autorizacion_iglesia = models.FileField(upload_to='static/autorizaciones/')
    activo = models.BooleanField(default=True)  # Campo para marcar como activo o inactivo


    def __str__(self):
        return f'{self.apellido}, {self.nombres} ({self.dni})'
