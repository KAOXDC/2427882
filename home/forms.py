
from django import forms
from .models import Producto
class contact_form (forms.Form):
    asunto = forms.CharField(widget = forms.TextInput())
    correo = forms.EmailField(widget = forms.TextInput())
    texto = forms.CharField(widget = forms.Textarea())

class agregar_producto_form (forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
        exclude = ['status']

