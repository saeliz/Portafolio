"""
Vistas del portafolio - Controladores que procesan las peticiones
"""

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Proyecto, Estadistica, Habilidad
from .forms import FormularioContacto


def inicio(peticion):
    """
    Vista principal - renderiza toda la página del portafolio
    Obtiene proyectos, estadísticas y habilidades desde la base de datos
    """
    # Proyectos destacados para la sección principal
    proyectos = Proyecto.objects.all()

    # Estadísticas para los contadores animados
    estadisticas = Estadistica.objects.all()

    # Habilidades técnicas para las barras de progreso
    habilidades = Habilidad.objects.all()

    # Formulario de contacto vacío
    formulario = FormularioContacto()

    contexto = {
        'proyectos': proyectos,
        'estadisticas': estadisticas,
        'habilidades': habilidades,
        'formulario': formulario,
        'total_proyectos': proyectos.count(),
    }

    return render(peticion, 'portfolio_app/inicio.html', contexto)


def enviar_contacto(peticion):
    """
    Vista que procesa el formulario de contacto (solo POST)
    Guarda el mensaje en la BD - visible en /admin/portfolio_app/mensajecontacto/
    """
    if peticion.method == 'POST':
        formulario = FormularioContacto(peticion.POST)
        if formulario.is_valid():
            # Guarda el mensaje en la base de datos
            formulario.save()
            messages.success(peticion, '¡Mensaje enviado! Me pondré en contacto pronto.')
        else:
            messages.error(peticion, 'Por favor revisa los campos del formulario.')

    return redirect('inicio')
