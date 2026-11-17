from django.contrib import admin
from .models import Marca, Luchador

@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripcion')
    list_filter = ('nombre',)
    search_fields = ('nombre', 'descripcion')

@admin.register(Luchador)
class LuchadorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre_ring', 'marca', 'peso_kg', 'fecha_debut', 'es_campeon')
    list_filter = ('marca', 'es_campeon')
    search_fields = ('nombre_ring',)