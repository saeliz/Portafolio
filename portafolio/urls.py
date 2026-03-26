"""
URLs principales del proyecto - enruta hacia la app portfolio_app
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Panel de administración de Django - accesible en /admin/
    # Desde aquí puedes agregar/editar proyectos, mensajes de contacto, etc.
    path('admin/', admin.site.urls),

    # Todas las demás URLs van a portfolio_app
    path('', include('portfolio_app.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
