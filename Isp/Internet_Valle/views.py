#from django.shortcuts import render
#from django.views.generic.list import ListView
from django.urls import reverse_lazy

from .models import *
from .forms import *
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import DetailView, ListView
#from django.contrib import messages


# Create your views here.

################### CLIENTE ###################

class ClienteCreateView(CreateView):
    model = Cliente
    template_name = 'cliente_form.html'
    form_class = ClienteForm
    success_url = reverse_lazy('apli:ClienteListar')

class ClienteUpdateView(UpdateView):
    model = Cliente
    form_class = ClienteForm
    #success_url = reverse_lazy('cliente:cliente_listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Modificar Cliente"
        return context

class ClienteListar(ListView):
    model=Cliente
    template_name = 'cliente_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = Cliente.objects.all()
        return context
################### Servicio ###################

class ServicioCreateView(CreateView):
    model = Servicio
    form_class = ServicioForm
    template_name = 'servicio_form.html'
    success_url = reverse_lazy('apli:ServicioListar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Alta de Servicio"
        return context

class ServicioUpdateView(UpdateView):
    model = Servicio
    #form_class = FormularioServicio
   # success_url = reverse_lazy('servicio:servicio_crear')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Modificar Servicio"
        return context
    
    def form_valid(self, form):
       # messages.add_message(self.request, messages.SUCCESS, 'Servicio con éxito')
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        print(form.non_field_errors())
        #messages.add_message(self.request, messages.ERROR, form.errors)
        return super().form_invalid(form)

class ServicioDetailView (DetailView):
    model = Servicio

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Servicio"
        return context

class ServicioListar(ListView):
    model=Servicio
    template_name = 'Servicio_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = Servicio.objects.all()
        return context
    
################### Equipo ###################

class EquipoCreateView(CreateView):
    model = Equipo
    form_class = EquipoForm
    template_name = "equipo_form.html"
   # success_url = reverse_lazy('equipo:equipo_crear')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Alta de Equipo"
        return context

class EquipoUpdateView(UpdateView):
    model = Equipo
     #form_class = FormularioEquipo
   # success_url = reverse_lazy('equipo:equipo_crear')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Modificar Equipo"
        return context
    
    def form_valid(self, form):
       # messages.add_message(self.request, messages.SUCCESS, 'Equipo modificada con éxito')
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        print(form.non_field_errors())
       # messages.add_message(self.request, messages.ERROR, form.errors)
        return super().form_invalid(form)

class EquipoDetailView (DetailView):
    model = Equipo

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Equipo"
        return context

class EquipoListar(ListView):
    model=Equipo
    template_name = 'equipo_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = Equipo.objects.all()
        return context    
 ################### Contrato ###################
class ContratoCreateView(CreateView):
    model = Contrato
    form_class = ContratoForm
    template_name = "contrato_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Alta de Contrato"
        return context

class ContratoUpdateView(UpdateView):
    model = Contrato
    #form_class = FormularioContrato
   # success_url = reverse_lazy('contrato:contrato_crear')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Modificar Contrato"
        return context
    
    def form_valid(self, form):
       # messages.add_message(self.request, messages.SUCCESS, 'Contrato modificada con éxito')
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        print(form.non_field_errors())
        #messages.add_message(self.request, messages.ERROR, form.errors)
        return super().form_invalid(form)

class ContratoDetailView (DetailView):
    model = Contrato

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Contrato"
        return context

class ContratoListar(ListView):
    model=Contrato
    template_name = 'contrato_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = Contrato.objects.all()
        return context      
    
################### Pago ###################
class PagoCreateView(CreateView):
    model = Pago
    form_class = PagoForm
    template_name = "pago_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Alta de Pago"
        return context

class PagoUpdateView(UpdateView):
    model = Pago
    #form_class = FormularioPago
   # success_url = reverse_lazy('pago:pago_crear')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Modificar pago"
        return context
    
    def form_valid(self, form):
       # messages.add_message(self.request, messages.SUCCESS, 'pago modificada con éxito')
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        print(form.non_field_errors())
        #messages.add_message(self.request, messages.ERROR, form.errors)
        return super().form_invalid(form)

class PagoDetailView (DetailView):
    model = Pago

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Pago"
        return context

################### Detalle_Pago ###################

class Detalle_PagoCreateView(CreateView):
    model = Detalle_Pago
    #form_class = AdicionalForm
    #template_name = "adicional_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Alta de Detalle de Pago"
        return context

class Detalle_PagoUpdateView(UpdateView):
    model = Detalle_Pago
    #form_class = FormularioDetalle_Pago
   # success_url = reverse_lazy('detalle_pago:detalle_pago_crear')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Modificar detalle de pago"
        return context
    
    def form_valid(self, form):
        #messages.add_message(self.request, messages.SUCCESS, 'detalle de pago modificada con éxito')
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        print(form.non_field_errors())
       # messages.add_message(self.request, messages.ERROR, form.errors)
        return super().form_invalid(form)

class Detalle_PagoDetailView (DetailView):
    model = Detalle_Pago

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "detalle de pago"
        return context
   
    

################### Adicional ###################
class AdicionalCreateView(CreateView):
    model = Adicional
    form_class = AdicionalForm
    template_name = "adicional_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Alta de Adicional"
        return context

class AdicionalUpdateView(UpdateView):
    model = Adicional
    #form_class = FormularioAdicional
   # success_url = reverse_lazy('adicional:adicional_crear')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Modificar adicional"
        return context
    
    def form_valid(self, form):
        #messages.add_message(self.request, messages.SUCCESS, 'adicional modificado con éxito')
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        print(form.non_field_errors())
        #messages.add_message(self.request, messages.ERROR, form.errors)
        return super().form_invalid(form)

class AdicionalDetailView (DetailView):
    model = Adicional

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "detalle Adicional"
        return context
   
   