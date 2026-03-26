"""
Formularios de la app - Formulario de contacto
"""

from django import forms
from .models import MensajeContacto


class FormularioContacto(forms.ModelForm):
    """
    Formulario de contacto que guarda mensajes en la base de datos
    Los mensajes son visibles en el admin: /admin/portfolio_app/mensajecontacto/
    """
    class Meta:
        model = MensajeContacto
        fields = ['nombre', 'email', 'asunto', 'mensaje']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'campo-formulario',
                'placeholder': 'Tu nombre completo'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'campo-formulario',
                'placeholder': 'tu@email.com'
            }),
            'asunto': forms.TextInput(attrs={
                'class': 'campo-formulario',
                'placeholder': '¿En qué puedo ayudarte?'
            }),
            'mensaje': forms.Textarea(attrs={
                'class': 'campo-formulario',
                'placeholder': 'Cuéntame sobre tu proyecto...',
                'rows': 5
            }),
        }
