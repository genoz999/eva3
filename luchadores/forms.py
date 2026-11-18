from django import forms
from .models import Luchador

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