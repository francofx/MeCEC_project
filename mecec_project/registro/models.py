from django.db import models

class Registro(models.Model):
    apellido = models.CharField(max_length=100)
    nombres = models.CharField(max_length=100)
    dni = models.CharField(max_length=20)
    fecha_nac = models.DateField()
    ciudad = models.CharField(max_length=100)
    provincia = models.CharField(max_length=100)
    nombre_apellido_paterno = models.CharField(max_length=100)
    nombre_apellido_materno = models.CharField(max_length=100)
    celular = models.CharField(max_length=20)
    domicilio_actual = models.CharField(max_length=255)
    correo_electronico = models.EmailField()
    foto = models.ImageField(upload_to='fotos/')
    ministerio = models.CharField(max_length=100)
    registro = models.CharField(max_length=100)
    tipo_pabellon = models.CharField(max_length=100)
    numero_pabellon = models.CharField(max_length=100)
    seccion_pabellon = models.CharField(max_length=100)
    otros_pabellon = models.CharField(max_length=255, blank=True, null=True)
    autorizacion_iglesia = models.FileField(upload_to='autorizaciones/')

    def __str__(self):
        return f'{self.apellido}, {self.nombres} ({self.dni})'