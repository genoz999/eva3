from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.db.models import Count
from .models import Luchador, Marca
from .forms import LuchadorForm, CampeonatoFormSet


class LuchadorListView(ListView):
    model = Luchador
    template_name = 'luchadores/luchador_list.html'
    context_object_name = 'luchadores'

    def get_queryset(self):
        queryset = Luchador.objects.select_related('marca').order_by('nombre_ring')
        marca = self.request.GET.get('marca', '').strip()
        busqueda = self.request.GET.get('q', '').strip()

        if marca:
            if marca.isdigit():
                queryset = queryset.filter(marca_id=marca)
            else:
                queryset = queryset.filter(marca__nombre__iexact=marca)
        if busqueda:
            queryset = queryset.filter(nombre_ring__icontains=busqueda)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_luchadores'] = Luchador.objects.count()
        context['total_campeones'] = Luchador.objects.filter(es_campeon=True).count()
        context['marcas'] = Marca.objects.annotate(total=Count('luchadores'))
        context['q'] = self.request.GET.get('q', '').strip()
        context['marca_seleccionada'] = self.request.GET.get('marca', '').strip()
        return context


class LuchadorDetailView(DetailView):
    model = Luchador
    template_name = 'luchadores/luchador_detail.html'
    context_object_name = 'luchador'

    def get_queryset(self):
        return Luchador.objects.select_related('marca').prefetch_related('campeonatos')


class LuchadorCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Luchador
    form_class = LuchadorForm
    template_name = 'luchadores/luchador_form.html'
    success_url = reverse_lazy('luchador_list')
    success_message = "Luchador '%(nombre_ring)s' registrado exitosamente."

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['campeonatos_formset'] = CampeonatoFormSet(self.request.POST)
        else:
            context['campeonatos_formset'] = CampeonatoFormSet()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        campeonatos_formset = context['campeonatos_formset']
        if campeonatos_formset.is_valid():
            self.object = form.save()
            campeonatos_formset.instance = self.object
            campeonatos_formset.save()
            return super().form_valid(form)
        return self.form_invalid(form)


class LuchadorUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Luchador
    form_class = LuchadorForm
    template_name = 'luchadores/luchador_form.html'
    success_url = reverse_lazy('luchador_list')
    success_message = "Datos de '%(nombre_ring)s' actualizados correctamente."

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['campeonatos_formset'] = CampeonatoFormSet(self.request.POST, instance=self.object)
        else:
            context['campeonatos_formset'] = CampeonatoFormSet(instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        campeonatos_formset = context['campeonatos_formset']
        if campeonatos_formset.is_valid():
            self.object = form.save()
            campeonatos_formset.instance = self.object
            campeonatos_formset.save()
            return super().form_valid(form)
        return self.form_invalid(form)


class LuchadorDeleteView(LoginRequiredMixin, DeleteView):
    model = Luchador
    template_name = 'luchadores/luchador_confirm_delete.html'
    success_url = reverse_lazy('luchador_list')

    def form_valid(self, form):
        messages.success(self.request, f"El luchador '{self.object.nombre_ring}' fue eliminado del roster.")
        return super().form_valid(form)