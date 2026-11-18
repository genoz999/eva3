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
    foto_url = models.URLField(max_length=500, blank=True, null=True, verbose_name="URL de la Foto")

    def __str__(self):
        return f"{self.nombre_ring} ({self.marca.nombre})"

    class Meta:
        verbose_name = "Luchador"
        verbose_name_plural = "Luchadores"

foto_url = models.URLField(max_length=500, blank=True, null=True, verbose_name="URL de la Foto")

class Campeonato(models.Model):
    luchador = models.ForeignKey(Luchador, on_delete=models.CASCADE, related_name='campeonatos')
    titulo = models.CharField(max_length=120, verbose_name="Nombre del Título")
    fecha_ganado = models.DateField(verbose_name="Fecha en que lo ganó")
    reinados = models.PositiveIntegerField(default=1, verbose_name="N° de Reinados")
    dias_reinado = models.PositiveIntegerField(default=0, verbose_name="Días de Reinado")
    es_actual = models.BooleanField(default=False, verbose_name="¿Lo posee actualmente?")

    class Meta:
        ordering = ['-es_actual', '-fecha_ganado']
        verbose_name = "Campeonato"
        verbose_name_plural = "Campeonatos"

    def __str__(self):
        return f"{self.titulo} ({self.luchador.nombre_ring})"

    class Meta:
        ordering = ['-es_actual', '-fecha_ganado']
        verbose_name = "Campeonato"
        verbose_name_plural = "Campeonatos"

    def __str__(self):
        return f"{self.titulo} ({self.luchador.nombre_ring})"