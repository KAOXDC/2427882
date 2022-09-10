
from django import forms

class contact_form (forms.Form):
    asunto = forms.CharField(widget = forms.TextInput())
    correo = forms.EmailField(widget = forms.TextInput())
    texto = forms.CharField(widget = forms.Textarea())
