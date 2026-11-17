from django.db import models

class Marca(models.Model):
    nombre = models.CharField(max_length=50, unique=True, verbose_name="Nombre de la marca")
    descripcion = models.TextField(blank=True, null=True, verbose_name="Descripcion")
    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Marca"
        verbose_name_plural = "Marcas"

class Luchador(models.Model):
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE, related_name='luchadores', verbose_name="Marca")
    nombre_ring = models.CharField(max_length=100, verbose_name="Nombre en el Ring")
    peso_kg = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Peso (kg)")
    fecha_debut = models.DateField(verbose_name="Fecha de Debut")
    es_campeon = models.BooleanField(default=False, verbose_name="¿Es Canpeón Actual?")

    def __str__(self):
        return f"{self.nombre_ring} ({self.marca.nombre})"

    class Meta:
        verbose_name = "Luchador"
        verbose_name_plural = "Luchadores"