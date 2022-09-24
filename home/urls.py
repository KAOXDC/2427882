from django.urls import path
from .views import *

urlpatterns = [
    path('sobre-nosotros/', vista_about , name = 'about'),
    path('contacto/', vista_contact , name = 'contact'),
    path('', vista_inicio , name = 'inicio'),
    path('agregar_producto/', vista_agregar_producto , name = 'agregar_producto'),
    path('listar_productos/', vista_listar_productos , name = 'listar_productos'),
    
]