from django import forms
from .models import Luchador

class LuchadorForm(forms.ModelForm):
    class Meta:
        model = Luchador
        fields = ['marca', 'nombre_ring', 'peso_kg', 'fecha_debut', 'es_campeon']
        widgets = {
            'marca': forms.Select(attrs={'class': 'form-select'}),
            'nombre_ring': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Cody Rhodes'}),
            'peso_kg': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'placeholder': 'Ej: 99.80'}),
            'fecha_debut': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'es_campeon': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }