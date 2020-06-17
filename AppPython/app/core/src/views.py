from django.views.generic.base import TemplateView
from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse
from .forms import ContactForm
from django.core.mail import EmailMessage
# Create your views here.

class HomePageView(TemplateView):

    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'btn1':'Inicio', 'btn2':'Sobre SAV', 'btn3':'Características', 'btn4':'Objetivo', 'btn5':'Nosotros', 'btn6':'Contacto', 'btn7': 'Presentación', 'tituloIni':'SISTEMA DE GESTIÓN VIRTUAL DE APRENDICES', 'tituloNosotros': 'Sobre SAV','spanUno': '1', 'tituloSAV':'SAV', 'txt1':'SAV es un aplicativo web dirigido al área de contrato de aprendizaje del SENA, este ayudará a los trabajadores de esta área a organizar una base de datos con información de aprendices que cuentan o no con una alternativa para la etapa productiva; con este aplicativo se podrá ver la información en conjunto como programa de Formación y/o ficha como también la información de un aprendiz en particular lo que brindará un apoyo más rápido y eficaz para la búsqueda de tal información a los usuarios.', 'tituloCaracteristicas': 'Características', 'tituloEficaz':'Eficaz', 'txt2': 'Adaptado para una buena búsqueda de la información.', 'tituloSeguro':'Seguro', 'txt3':'Cuida la información de cada uno de los usuarios permitiendo que sea un sitio web confiable.', 'tituloOrganizado':'Organizado', 'txt4': 'Diseño sencillo y modelado para una mayor facilidad de uso.', 'tituloObjetivo':'Objetivo', 'txt5':'Permitir administrar la información y la gestión documental pertinente a los procesos de seguimiento de alternativas al Contrato de Aprendizaje, tanto en la fase lectiva como en la fase productiva.', 'txt6':'SENA 2020 ', 'txt7':'Denisse Alejandra Alzate Meneses | Sergio León Saldarriaga Dávila | Laura Vanessa Agudelo Arias' })

class NosotrosPageView(TemplateView):

    template_name = "nosotros.html"

    def get(self,request, *args, **kwargs):
       return render(request, self.template_name, {'btn1':'Inicio', 'btn2':'Nosotros', 'btn3':'Contacto', 'btn4': 'Presentación', 'texto':'¡CONOCE A NUESTRO EQUIPO DE DESARROLLADORES!', 'tituloNosotros':'Nosotros','integranteUno':'Denisse Alejandra', 'integranteDos':'Sergio León', 'integranteTres':'Laura Vanessa','txt1': 'Web Designer', 'txt2':'Backend Developer' ,'txt3':'Estudiantes del Sena en Análisis y Desarrollo de Sistemas de información Graduados como técnicos en sistemas', 'txt4':'denalme609@gmail.com', 'txt5':'sergiosaldarriagadavila@gmail.com', 'txt6':'lauraagudelo102001@gmail.com', 'txt7':'SENA 2020 ', 'txt8':'Denisse Alejandra Alzate Meneses | Sergio León Saldarriaga Dávila | Laura Vanessa Agudelo Arias' })

class PresentacionPageView(TemplateView):

    template_name = "presentacion.html"

    def get(self,request, *args, **kwargs):
        return render(request, self.template_name, {'btn1':'Inicio', 'btn2':'Nosotros', 'btn3':'Contacto', 'btn4': 'Presentación', 'txt1': '¡CONOCE MÁS ACERCA DE SAV!', 'tituloUno': 'Esquema de la Base de Datos|SAV', 'txt2': 'SENA', 'txt3':'Denisse Alejandra Alzate Meneses | Sergio León Saldarriaga Dávila | Laura Vanessa Agudelo Arias'})

def contacto(request):
        formContact = ContactForm()

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

        #'btn1':'Inicio', 'btn2':'Nosotros', 'btn3':'Contacto', 'btn4': 'Presentación', 'txt1': '¡CONTÁCTATE CON NOSOTROS!', 'tituloContacto': '¡CONTÁCTANOS!', 'txt2':'Carrera 68 #104, Complejo Norte, Medellín, Antioquia', 'txt3':'sav_sena@correo.com', 'txt4':'3148867898', 'btn8':'Enviar', 'txt5':'SENA 2020 ', 'txt6':'Denisse Alejandra Alzate Meneses | Sergio León Saldarriaga Dávila | Laura Vanessa Agudelo Arias'