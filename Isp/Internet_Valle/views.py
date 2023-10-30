from django.shortcuts import render
from django.views.generic.list import ListView
from .models import *
from .forms import *
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.template import loader
from django.http import HttpResponse
from datetime import datetime  

from django.urls import reverse_lazy
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect
# Create your views here.

################### CLIENTE ###################

class ClienteCreateView(CreateView):
    model = Cliente
    #form_class = FormularioCliente
   # success_url = reverse_lazy('cliente:cliente_crear')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Alta de Cliente"
        return context

class ClienteUpdateView(UpdateView):
    model = Cliente
    #form_class = FormularioCliente
    #success_url = reverse_lazy('cliente:cliente_listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Modificar Cliente"
        return context
    
    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS, 'Cliente modificada con éxito')
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        print(form.non_field_errors())
        messages.add_message(self.request, messages.ERROR, form.errors)
        return super().form_invalid(form)

class ClienteDetailView (DeleteView):
    model = Cliente

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Cliente"
        return context

################### CLIENTE ###################