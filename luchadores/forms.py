from django import forms
from django.forms import inlineformset_factory
from .models import Luchador, Campeonato


class LuchadorForm(forms.ModelForm):
    class Meta:
        model = Luchador
        fields = ['nombre_ring', 'marca', 'peso_kg', 'fecha_debut', 'es_campeon', 'foto_url']
        widgets = {
            'nombre_ring': forms.TextInput(attrs={'class': 'form-control'}),
            'marca': forms.Select(attrs={'class': 'form-select'}),
            'peso_kg': forms.NumberInput(attrs={'class': 'form-control'}),
            'fecha_debut': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'es_campeon': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'foto_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://ejemplo.com/foto.jpg'}),
        }


CampeonatoFormSet = inlineformset_factory(
    Luchador,
    Campeonato,
    fields=['titulo', 'reinados', 'fecha_ganado', 'es_actual'],
    extra=1,
    can_delete=True,
    widgets={
        'titulo': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Ej: WWE Championship'}),
        'reinados': forms.NumberInput(attrs={'class': 'form-control form-control-sm', 'min': 1}),
        'fecha_ganado': forms.DateInput(attrs={'class': 'form-control form-control-sm', 'type': 'date'}),
        'es_actual': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
    }
)