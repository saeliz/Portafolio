"""
Modelos de la base de datos del portafolio
Cada modelo representa una tabla en la BD gestionable desde el admin de Django
"""

from django.db import models


class Categoria(models.Model):
    """
    Categoría de proyecto (ej: Web, Mobile, Backend)
    Administrable desde: /admin/portfolio_app/categoria/
    """
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    color = models.CharField(max_length=7, default="#F2A68A", verbose_name="Color hex")

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"

    def __str__(self):
        return self.nombre


class Proyecto(models.Model):
    """
    Modelo principal de proyectos del portafolio
    Administrable desde: /admin/portfolio_app/proyecto/
    Los proyectos que aquí se creen aparecerán automáticamente en la web
    """
    titulo = models.CharField(max_length=200, verbose_name="Título")
    descripcion = models.TextField(verbose_name="Descripción")
    categoria = models.ForeignKey(
        Categoria, on_delete=models.SET_NULL,
        null=True, blank=True, verbose_name="Categoría"
    )
    imagen = models.ImageField(
        upload_to='proyectos/', blank=True, null=True,
        verbose_name="Imagen del proyecto"
    )
    url_demo = models.URLField(blank=True, verbose_name="URL Demo")
    url_github = models.URLField(blank=True, verbose_name="URL GitHub")
    tecnologias = models.CharField(
        max_length=300, blank=True,
        verbose_name="Tecnologías (separadas por coma)"
    )
    destacado = models.BooleanField(default=False, verbose_name="¿Destacado?")
    orden = models.PositiveIntegerField(default=0, verbose_name="Orden de aparición")
    fecha_creacion = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"
        ordering = ['orden', '-fecha_creacion']

    def __str__(self):
        return self.titulo

    def lista_tecnologias(self):
        """Retorna las tecnologías como lista para el template"""
        return [t.strip() for t in self.tecnologias.split(',') if t.strip()]


class Estadistica(models.Model):
    """
    Estadísticas del portafolio (proyectos, clientes, años de experiencia)
    Administrable desde: /admin/portfolio_app/estadistica/
    """
    icono = models.CharField(max_length=50, verbose_name="Icono (clase CSS)")
    numero = models.PositiveIntegerField(verbose_name="Número")
    etiqueta = models.CharField(max_length=100, verbose_name="Etiqueta")
    orden = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Estadística"
        verbose_name_plural = "Estadísticas"
        ordering = ['orden']

    def __str__(self):
        return f"{self.numero} {self.etiqueta}"


class Habilidad(models.Model):
    """
    Habilidades técnicas del desarrollador
    Administrable desde: /admin/portfolio_app/habilidad/
    """
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    porcentaje = models.PositiveIntegerField(default=80, verbose_name="Porcentaje (%)")
    orden = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Habilidad"
        verbose_name_plural = "Habilidades"
        ordering = ['orden']

    def __str__(self):
        return self.nombre


class MensajeContacto(models.Model):
    """
    Mensajes enviados desde el formulario de contacto
    Administrable desde: /admin/portfolio_app/mensajecontacto/
    Todos los mensajes del formulario llegan aquí y son visibles en el admin
    """
    nombre = models.CharField(max_length=150, verbose_name="Nombre")
    email = models.EmailField(verbose_name="Email")
    asunto = models.CharField(max_length=200, verbose_name="Asunto")
    mensaje = models.TextField(verbose_name="Mensaje")
    leido = models.BooleanField(default=False, verbose_name="¿Leído?")
    fecha_envio = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de envío")

    class Meta:
        verbose_name = "Mensaje de Contacto"
        verbose_name_plural = "Mensajes de Contacto"
        ordering = ['-fecha_envio']

    def __str__(self):
        return f"{self.nombre} - {self.asunto}"
