from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Luchador
from .forms import LuchadorForm

class LuchadorListView(ListView):
    model = Luchador
    template_name = 'luchadores/luchador_list.html'
    context_object_name = 'luchadores'

    def get_queryset(self):
        # Optimización SQL: trae la Marca en la misma consulta (INNER JOIN)
        return Luchador.objects.select_related('marca').all().order_by('-es_campeon', 'nombre_ring')


class LuchadorCreateView(CreateView):
    model = Luchador
    form_class = LuchadorForm
    template_name = 'luchadores/luchador_form.html'
    success_url = reverse_lazy('luchador_list')


class LuchadorUpdateView(UpdateView):
    model = Luchador
    form_class = LuchadorForm
    template_name = 'luchadores/luchador_form.html'
    success_url = reverse_lazy('luchador_list')


class LuchadorDeleteView(DeleteView):
    model = Luchador
    template_name = 'luchadores/luchador_confirm_delete.html'
    success_url = reverse_lazy('luchador_list')