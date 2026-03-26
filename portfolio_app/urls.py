"""URLs de la app portfolio_app"""

from django.urls import path
from . import views as vistas

urlpatterns = [
    path('', vistas.inicio, name='inicio'),
    path('contacto/', vistas.enviar_contacto, name='enviar_contacto'),
]
