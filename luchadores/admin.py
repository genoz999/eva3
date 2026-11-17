from django.contrib import admin
from .models import Marca, Luchador

@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')

@admin.register(Luchador)
class LuchadorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre_ring', 'marca', 'peso_kg', 'fecha_debut', 'es_campeon')
    list_filter = ('es_campeon', 'marca')
    search_fields = ('nombre_ring',)