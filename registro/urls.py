
from django.urls import path
from registro import views
from . import views

app_name = 'registro'

urlpatterns = [
    
    path('', views.home, name="home"),
    path('formulario/', views.formulario, name='formulario'),
    path('listado/', views.listado_registros, name='listado_registros'),
    path('registro/<int:id>/', views.registro_detalle, name='registro_detalle'),
]
