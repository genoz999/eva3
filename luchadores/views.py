from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Luchador
from .forms import LuchadorForm


class LuchadorListView(ListView):
    model = Luchador
    template_name = 'luchadores/luchador_list.html'
    context_object_name = 'luchadores'

    def get_queryset(self):
        queryset = Luchador.objects.select_related('marca').order_by('nombre_ring')
        marca = self.request.GET.get('marca')
        busqueda = self.request.GET.get('q')

        if marca:
            queryset = queryset.filter(marca__nombre__iexact=marca)
        if busqueda:
            queryset = queryset.filter(nombre_ring__icontains=busqueda)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['marca_actual'] = self.request.GET.get('marca', '')
        context['busqueda_actual'] = self.request.GET.get('q', '')
        return context


class LuchadorDetailView(DetailView):
    model = Luchador
    template_name = 'luchadores/luchador_detail.html'
    context_object_name = 'luchador'


class LuchadorCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Luchador
    form_class = LuchadorForm
    template_name = 'luchadores/luchador_form.html'
    success_url = reverse_lazy('luchador_list')
    success_message = "Luchador '%(nombre_ring)s' registrado exitosamente."


class LuchadorUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Luchador
    form_class = LuchadorForm
    template_name = 'luchadores/luchador_form.html'
    success_url = reverse_lazy('luchador_list')
    success_message = "Datos de '%(nombre_ring)s' actualizados correctamente."


class LuchadorDeleteView(LoginRequiredMixin, DeleteView):
    model = Luchador
    template_name = 'luchadores/luchador_confirm_delete.html'
    success_url = reverse_lazy('luchador_list')

    def form_valid(self, form):
        messages.success(self.request, f"El luchador '{self.object.nombre_ring}' fue eliminado del roster.")
        return super().form_valid(form)