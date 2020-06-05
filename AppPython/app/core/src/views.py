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


#Vista basada en función

def contacto(request):
    formContact = ContactForm()
    if request.method =="POST":
        formContact = ContactForm(data=request.POST)
#validar que el formulario tenga una peticion POST:
    if request.method == "POST":
        formContact = ContactForm(data=request.POST)
        if formContact.is_valid():
            usuario = request.POST.get('usuario','')
            correo = request.POST.get('correo ','')
            tipomsj = request.POST.get('tipomsj','')
            mensaje = request.POST.get('mensaje','')

                #Objeto con las variables del formulario:
            email = EmailMessage(
                "RepoDevelopers: tienes un nuevo mensaje de contacto",
                "De {} <{}>\n\nEscribió:\n\n{}".format(usuario, correo, mensaje),
                "no-contestar@inbox.mailtrap.io",
                ["denalme609@gmail.com"],
                reply_to=[correo]
            )
                #Enviamos el correo:
            try:
                email.send()
                #se envia el correo:
                return redirect(reverse('contacto')+"?ok")
            except:
                #No se ha enviado el correo:
                return redirect(reverse('contacto')+"?fail")            

       
        return render(request, 'contacto.html', {'formulario':formContact, 'btn1':'Inicio', 'btn2':'Nosotros', 'btn3':'Contacto', 'btn4': 'Presentación', 'txt1': '¡CONTÁCTATE CON NOSOTROS!', 'tituloContacto': '¡CONTÁCTANOS!', 'txt2':'Carrera 68 #104, Complejo Norte, Medellín, Antioquia', 'txt3':'sav_sena@correo.com', 'txt4':'3148867898', 'btn8':'Enviar', 'txt5':'SENA 2020 ', 'txt6':'Denisse Alejandra Alzate Meneses | Sergio León Saldarriaga Dávila | Laura Vanessa Agudelo Arias'} ) 