
from django.urls import path
from registro import views
from . import views
#from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views

app_name = 'registro'

urlpatterns = [
    
    path('', views.home, name="home"),
    path('formulario/', views.formulario, name='formulario'),
    path('listado/', views.listado_registros, name='listado_registros'),
    path('registro/<int:id>/', views.registro_detalle, name='registro_detalle'),
    #path('logout/', LogoutView.as_view(next_page='/'), name='logout'),  # Redirige al home
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

]
