# 🎨 Portafolio Dev - Django + Tailwind CSS

Paleta pastel: Rosa suave • Verde menta • Durazno • Crema

## ⚡ Inicio rápido

```bash
# 1. Instalar dependencias
pip install django pillow

# 2. Migraciones
python manage.py makemigrations portfolio_app
python manage.py migrate

# 3. Cargar datos de ejemplo
python manage.py cargar_datos_ejemplo

# 4. Crear superusuario (para el admin)
python manage.py createsuperuser

# 5. Ejecutar servidor
python manage.py runserver
```

## 🔗 URLs importantes

| URL | Descripción |
|-----|-------------|
| `http://localhost:8000/` | Portafolio principal |
| `http://localhost:8000/admin/` | Panel Django Admin |
| `http://localhost:8000/admin/portfolio_app/proyecto/` | Gestionar proyectos |
| `http://localhost:8000/admin/portfolio_app/mensajecontacto/` | Ver mensajes de contacto |

## 📦 Estructura del proyecto

```
portafolio/
├── manage.py
├── portafolio/
│   ├── settings.py        # Configuración Django
│   └── urls.py            # URLs principales (incluye /admin/)
└── portfolio_app/
    ├── models.py           # Modelos BD (Proyecto, Estadistica, etc.)
    ├── views.py            # Vistas/controladores
    ├── admin.py            # Config del panel Admin Django
    ├── forms.py            # Formulario de contacto
    ├── urls.py             # URLs de la app
    ├── management/commands/
    │   └── cargar_datos_ejemplo.py
    └── templates/portfolio_app/
        └── inicio.html     # Template principal
```

## 🛠 Panel de administración Django

Login: `admin` / `admin123`

Desde el admin puedes:
- ✅ Agregar/editar/eliminar **proyectos** con imagen, tecnologías, links
- ✅ Gestionar **categorías** de proyectos
- ✅ Ajustar **estadísticas** (contadores animados)
- ✅ Ver y marcar como leídos los **mensajes de contacto**
- ✅ Gestionar **habilidades** y sus porcentajes

## 🎨 Paleta de colores (variables CSS)

```css
--rosa:    #F2D4CC   /* Rosa suave */
--menta:   #C8DDD6   /* Verde menta */
--durazno: #F2A68A   /* Durazno */
--crema:   #F5E6DF   /* Crema cálido */
```

## ✨ Funcionalidades UI

- 🌗 Modo oscuro/claro con localStorage
- 🎯 Cursor personalizado animado
- ⏳ Preloader antes de cargar
- 📊 Contadores animados (IntersectionObserver)
- 🎬 Animaciones AOS al hacer scroll
- 📱 Totalmente responsive
- 💬 Botón flotante de WhatsApp
- 🎨 Hover effects en tarjetas de proyectos
