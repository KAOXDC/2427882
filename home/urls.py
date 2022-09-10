from django.urls import path
from .views import *

urlpatterns = [
    path('sobre-nosotros/', vista_about , name = 'about'),
    path('contacto/', vista_contact , name = 'contact'),
    path('', vista_inicio , name = 'inicio'),
]