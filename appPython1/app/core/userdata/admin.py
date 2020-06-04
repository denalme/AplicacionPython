from django.contrib import admin
# Importamos las clases desde los modelos
from .models import Roles, DatosUser, HabilUser, DetaRoles, Rates

# Register your models here.
# Registro del modelo de Roles:
class RoleModel(admin.ModelAdmin):
    # Se indica qué columna se quiere ver
    list_display = ["RoleName"]
    # Se indica la columna en la que se puede hacer click para editar
    list_display_links = ["RoleName"]
    # Para agregar una barra de búsqueda
    # search_fields = ["RoleName"]
    # Se agrega un filtro
    list_filter = ["RoleName"]

    class Meta:
        model = Roles

admin.site.register(Roles)

# Registro del modelo de DatosUser:
class DatosUserModel(admin.ModelAdmin):
    list_display = ["nombUser"]

    list_display_links = ["nombUser","apelUser",]

    class Meta:
        model = DatosUser

admin.site.register(DatosUser)

# Registro del modelo de HabilUser
class HabilUserModel(admin.ModelAdmin):
    list_display = ["NombHabil"]

    class Meta:
        model = HabilUser

admin.site.register(HabilUser)

# Registro del modelo de DetaRoles
class DetaRolesModel(admin.ModelAdmin):
    list_display = ["idRole"]

    class Meta:
        model = DetaRoles

admin.site.register(DetaRoles)

# Registro del modelo de Rates
class RatesModel(admin.ModelAdmin):
    list_display = ["idUser"]

admin.site.register(Rates)
