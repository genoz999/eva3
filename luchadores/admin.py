from django.contrib import admin
from .models import Marca, Luchador, Campeonato

class CampeonatoInline(admin.TabularInline):
    model = Campeonato
    extra = 1

@admin.register(Luchador)
class LuchadorAdmin(admin.ModelAdmin):
    list_display = ('nombre_ring', 'marca', 'peso_kg', 'fecha_debut', 'es_campeon')
    list_filter = ('marca', 'es_campeon')
    search_fields = ('nombre_ring',)
    inlines = [CampeonatoInline]

@admin.register(Campeonato)
class CampeonatoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'luchador', 'reinados', 'fecha_ganado', 'es_actual')
    list_filter = ('es_actual', 'titulo')
    search_fields = ('titulo', 'luchador__nombre_ring')