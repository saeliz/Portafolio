"""
Configuración del panel de administración de Django
Accede en: http://localhost:8000/admin/
Crea un superusuario con: python manage.py createsuperuser
"""

from django.contrib import admin
from .models import Proyecto, Categoria, Estadistica, Habilidad, MensajeContacto

# Título personalizado del admin de Django
admin.site.site_header = "Portafolio Dev - Admin"
admin.site.site_title = "Portafolio"
admin.site.index_title = "Panel de Control"


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    """Admin para gestionar categorías de proyectos"""
    list_display = ['nombre', 'color']


@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    """
    Admin para gestionar proyectos del portafolio
    Desde aquí puedes agregar proyectos que aparecen en la web automáticamente
    """
    list_display = ['titulo', 'categoria', 'destacado', 'orden', 'fecha_creacion']
    list_filter = ['categoria', 'destacado']
    search_fields = ['titulo', 'descripcion', 'tecnologias']
    list_editable = ['destacado', 'orden']  # Editable directo en la lista


@admin.register(Estadistica)
class EstadisticaAdmin(admin.ModelAdmin):
    """Admin para gestionar los contadores animados"""
    list_display = ['etiqueta', 'numero', 'icono', 'orden']
    list_editable = ['numero', 'orden']


@admin.register(Habilidad)
class HabilidadAdmin(admin.ModelAdmin):
    """Admin para gestionar habilidades técnicas"""
    list_display = ['nombre', 'porcentaje', 'orden']
    list_editable = ['porcentaje', 'orden']


@admin.register(MensajeContacto)
class MensajeContactoAdmin(admin.ModelAdmin):
    """
    Admin para ver mensajes del formulario de contacto
    Los mensajes NO leídos aparecen resaltados
    """
    list_display = ['nombre', 'email', 'asunto', 'leido', 'fecha_envio']
    list_filter = ['leido', 'fecha_envio']
    list_editable = ['leido']
    readonly_fields = ['nombre', 'email', 'asunto', 'mensaje', 'fecha_envio']
    search_fields = ['nombre', 'email', 'asunto']
