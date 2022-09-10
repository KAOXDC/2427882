from django.shortcuts import render
from .forms import contact_form

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