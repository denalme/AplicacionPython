from django.views.generic.base import TemplateView
from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse
from .forms import ContactForm
from django.core.mail import EmailMessage

# Create your views here.

class HomePageView(TemplateView):

    template_name = "index.html"

    #def get_context_data(self, **kwargs):
     #   context = super().get_context_data(**kwargs)
      #  context['tituloIni'] = "Texto de Titulo"
       # return context
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'tituloIni':'Bu'} )

class NosotrosPageView(TemplateView):

    template_name = "nosotros.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'titulous':'Acerca de Nosotros', 'descripción':'Somos así'} )

#Vista basada en función

def contacto(request):
    formContact = ContactForm()

        #validar que el formulario tenga una peticion POST:
        if request.method == "POST":
            formContact = ContactForm(data=request.POST)
            if formContact.is_valid():
                usuario = request.POST.get('usuario','')
                correo  = request.POST.get('correo ','')
                tipomsj = request.POST.get('tipomsj','')
                mensaje = request.POST.get('mensaje','')
                return redirect(reverse('contacto')+"?ok")

        return render(request, 'contacto.html', {'formulario':formContact, 'btn1':'Inicio', 'btn2':'Nosotros', 'btn3':'Contacto', 'btn4': 'Presentación', 'txt1': '¡CONTÁCTATE CON NOSOTROS!', 'tituloContacto': '¡CONTÁCTANOS!', 'txt2':'Carrera 68 #104, Complejo Norte, Medellín, Antioquia', 'txt3':'sav_sena@correo.com', 'txt4':'3148867898', 'btn8':'Enviar', 'txt5':'SENA 2020 ', 'txt6':'Denisse Alejandra Alzate Meneses | Sergio León Saldarriaga Dávila | Laura Vanessa Agudelo Arias'} ) 

