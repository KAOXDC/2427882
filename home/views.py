from django.shortcuts import render, redirect
from .forms import contact_form, agregar_producto_form
from .models import *

# Create your views here.
def vista_inicio(request):
    return render(request, 'index.html', locals())


def vista_about (request):
    nombre = "Diego"
    apellido = "Prado"
    edad = 18
    estado = False
    # ctx = {'name': nombre, 'last_name' : apellido}
    return render(request, 'about.html', locals())

def vista_contact (request):
    
    if request.method == 'POST':
        form = contact_form(request.POST)
        if form.is_valid():
            a = form.cleaned_data('asunto')
            c = form.cleaned_data('correo')
            t = form.cleaned_data('texto')
            return render (request, 'contact.html', locals())
    else: # GET
        form = contact_form()

    return render(request, 'contact.html', locals())

def vista_agregar_producto(request):
    
    if request.method == 'POST':
        formulario = agregar_producto_form(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save() # INSERT INTO 'home_producto'  ....
            return redirect ('/')
    else: # GET
        formulario = agregar_producto_form()
    return render(request, 'producto_agregar.html', locals())


def vista_listar_productos(request):
    lista = Producto.objects.filter()

    return render(request, 'listar_productos.html', locals())