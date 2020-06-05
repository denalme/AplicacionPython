from django import forms
from .pqrsf import pqrsf

class ContactForm(forms.Form):

    #Atributos del formulario de contacto 
    usuario = forms.CharField(label="Nombre", required=True, widget=forms.TextInput(attrs={'class':'formulario', 'placeholder':'Nombre'}))
    correo = forms.EmailField(label="Correo Electrónico", required=True,widget=forms.EmailInput(attrs={'class':'formulario','placeholder':'Correo Electrónico'}))
    tipomsj = forms.ChoiceField(label="Asunto", required=True, choices=pqrsf, widget=forms.Select(attrs={'class','formulario'}))
    mensaje = forms.CharField(label="Mensaje", required=True, widget=forms.Textarea(attrs={'class':'formulario', 'rows':'5','placeholder':'Escribe tu Mensaje'}))
