from django.conf import settings
from django.db import models

# Create your models here.
class Comuna(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    region = models.CharField(max_length=100)
    activa = models.BooleanField(default=True)
    codigo_clasificacion = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f"{self.nombre} ({self.codigo_clasificacion} - {self.region})"


class inmobiliaria(models.Model):
    codigo_propiedad = models.CharField(max_length=10, unique=True)
    direccion = models.CharField(max_length=200)
    tipo_propiedad = models.CharField(choices=[('DEPARTAMENTO', 'Departamento'), ('CASA', 'Casa'), ('OFICINA', 'Oficina')], max_length=20)
    precio_arriendo = models.DecimalField(max_digits=10, decimal_places=2)
    dormitorios = models.IntegerField()
    baños = models.IntegerField()
    disponible = models.BooleanField(default=True)
    fecha_publicacion = models.DateField(auto_now_add=True)
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE, related_name='propiedades')
    inmobiliaria_comuna = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="propiedades",
    )

    def __str__(self):
        return f"{self.codigo_propiedad} - {self.tipo_propiedad} - {self.direccion}"
