"""
Comando Django para cargar datos de ejemplo en la base de datos
Ejecutar con: python manage.py cargar_datos_ejemplo
"""

from django.core.management.base import BaseCommand
from portfolio_app.models import Proyecto, Categoria, Estadistica, Habilidad


class Command(BaseCommand):
    help = 'Carga datos de ejemplo para el portafolio'

    def handle(self, *args, **options):
        self.stdout.write('Cargando datos de ejemplo...')

        # Crear categorías
        cat_web, _ = Categoria.objects.get_or_create(nombre='Web App', defaults={'color': '#F2A68A'})
        cat_mobile, _ = Categoria.objects.get_or_create(nombre='Mobile', defaults={'color': '#C8DDD6'})
        cat_api, _ = Categoria.objects.get_or_create(nombre='API REST', defaults={'color': '#F2D4CC'})

        # Crear proyectos de ejemplo
        proyectos_ejemplo = [
            {
                'titulo': 'E-commerce Platform',
                'descripcion': 'Plataforma de comercio electrónico completa con carrito de compras, pagos y panel de administración.',
                'categoria': cat_web,
                'tecnologias': 'Django, PostgreSQL, React, Stripe',
                'url_github': 'https://github.com',
                'destacado': True,
                'orden': 1,
            },
            {
                'titulo': 'API de Delivery',
                'descripcion': 'API REST para aplicación de delivery con tracking en tiempo real y notificaciones push.',
                'categoria': cat_api,
                'tecnologias': 'Django REST Framework, Redis, Celery, Docker',
                'url_github': 'https://github.com',
                'destacado': True,
                'orden': 2,
            },
            {
                'titulo': 'Dashboard Analytics',
                'descripcion': 'Panel de métricas y analíticas en tiempo real para empresas con visualizaciones interactivas.',
                'categoria': cat_web,
                'tecnologias': 'Django, Chart.js, PostgreSQL, Tailwind',
                'url_demo': 'https://demo.com',
                'orden': 3,
            },
        ]

        for datos in proyectos_ejemplo:
            Proyecto.objects.get_or_create(titulo=datos['titulo'], defaults=datos)

        # Crear estadísticas para los contadores
        estadisticas_ejemplo = [
            {'icono': '📁', 'numero': 20, 'etiqueta': 'Proyectos', 'orden': 1},
            {'icono': '👥', 'numero': 15, 'etiqueta': 'Clientes', 'orden': 2},
            {'icono': '⭐', 'numero': 4, 'etiqueta': 'Años de experiencia', 'orden': 3},
            {'icono': '✅', 'numero': 100, 'etiqueta': '% Satisfacción', 'orden': 4},
        ]

        for datos in estadisticas_ejemplo:
            Estadistica.objects.get_or_create(etiqueta=datos['etiqueta'], defaults=datos)

        # Crear habilidades
        habilidades_ejemplo = [
            {'nombre': 'Python / Django', 'porcentaje': 92, 'orden': 1},
            {'nombre': 'JavaScript / React', 'porcentaje': 85, 'orden': 2},
            {'nombre': 'PostgreSQL', 'porcentaje': 80, 'orden': 3},
            {'nombre': 'Docker / DevOps', 'porcentaje': 72, 'orden': 4},
            {'nombre': 'UI/UX Design', 'porcentaje': 68, 'orden': 5},
            {'nombre': 'REST APIs', 'porcentaje': 90, 'orden': 6},
        ]

        for datos in habilidades_ejemplo:
            Habilidad.objects.get_or_create(nombre=datos['nombre'], defaults=datos)

        self.stdout.write(self.style.SUCCESS('✅ Datos de ejemplo cargados exitosamente'))
        self.stdout.write('Accede al admin en: http://localhost:8000/admin/')
