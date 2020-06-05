from django.contrib import admin
# Importamos las clases desde los modelos
from .models import CategProye, Proyectos, TipoDocu, Documentos

# Register your models here.
# Registro del modelo de Roles:
class CategProyeModel(admin.ModelAdmin):
    # Se indica qué columna se quiere ver
    list_display = ["Lenguaje"]
    # Se indica la columna en la que se puede hacer click para editar
    list_display_links = ["Lenguaje"]
    # Para agregar una barra de búsqueda
    # search_fields = ["RoleName"]
    # Se agrega un filtro
    list_filter = ["Lenguaje"]

    class Meta:
        model = CategProye

admin.site.register(CategProye)

# Registro del modelo de DatosUser:
class ProyectosModel(admin.ModelAdmin):
    list_display = ["NombProy"]

    class Meta:
        model = Proyectos

admin.site.register(Proyectos)

# Registro del modelo de HabilUser
class TipoDocuModel(admin.ModelAdmin):
    list_display = ["NombTiDoc"]

    class Meta:
        model = TipoDocu

admin.site.register(TipoDocu)

# Registro del modelo de DetaRoles
class DocumentosModel(admin.ModelAdmin):
    list_display = ["NombDocu"]

    class Meta:
        model = Documentos

admin.site.register(Documentos)
