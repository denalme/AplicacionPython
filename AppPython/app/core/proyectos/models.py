from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField
from userdata.models import DatosUser

# Create your models here.
# Estructura de la aplicacion en el modelo de datos

#Modelo de la tabla Roles:
class CategProye(models.Model):
    Lenguaje = models.CharField(max_length = 50, verbose_name = "Lenguaje")
    MotorDB = models.CharField(max_length = 155, verbose_name = "Motor de Base De Datos")
    Arquitectura = models.CharField(max_length = 255, verbose_name = "Arquitectura") 

    class Meta:
        verbose_name = "Categoria del Proyecto"
        verbose_name_plural = "Categorias"

    # Creo la función para llamar atributos:
    def __str__(self):
        return self.Lenguaje

# Modelo de la tabla Proyectos
class Proyectos(models.Model):
    idCategProye = models.ForeignKey(CategProye, on_delete = models.CASCADE)
    NombProyect = models.CharField(max_length = 45, verbose_name = "Nombre Del Proyecto")
    descproyect = models.TextField(verbose_name="Descripción del proyecto")
    logoProyect = models.ImageField(upload_to='img/proyectos', verbose_name = "Icono")
    FechaIni = models.DateTimeField(auto_now_add = False, auto_now= False, verbose_name="Fecha de Inicio")
    FechaFin = models.DateTimeField(auto_now_add = False, auto_now= False, verbose_name="Fecha de Finalización")
    UrlRepo = models.TextField(verbose_name = "Url del Repositorio")
    EstaProy = models.CharField(max_length = 45, verbose_name = "Estado del Proyecto")

    class Meta:
        verbose_name = "Proyectos de Usuarios"
        verbose_name_plural = "Proyectos y Experiencias"

    def __str__(self):
        return self.NombProyect

# Modelo de la tabla TipoDocu
class TipoDocu(models.Model):
    NombTiDoc = models.CharField(max_length = 45, verbose_name = "Nombre Tipo Documento")

    class Meta:
        verbose_name = "Tipo Documento"
        verbose_name_plural = "Tipos de Documentos"

    def __str__(self):
        return self.NombTiDoc

# Modelo de la tabla Documentos
class Documentos(models.Model):
    idTipoDocu = models.ForeignKey(TipoDocu, on_delete = models.CASCADE)
    idProyectos = models.ForeignKey(Proyectos, on_delete = models.CASCADE)
    idUsuarios = models.ForeignKey(DatosUser, on_delete = models.CASCADE)
    NombDocu = models.CharField(max_length = 50, verbose_name = "Nombre Del Documento")
    PathDocu = models.CharField(max_length = 50, verbose_name = "Ruta de Almacenamiento del Documento")

    class Meta:
        verbose_name = "Documento"
        verbose_name_plural = "Documentos"

    def __str__(self):
        return self.NombDocu
