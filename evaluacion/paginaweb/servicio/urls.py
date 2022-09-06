from django.urls import path

from .views import CrearServicio, servicio


urlpatterns = [
   
   
    path('',servicio, name="Servicio"),
    path('crear_servicio',CrearServicio.as_view(), name = 'crear_servicio'),
   
    
]