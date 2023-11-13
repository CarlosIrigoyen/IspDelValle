from cProfile import label
from dataclasses import fields
from pyexpat import model
#from tkinter.ttk import Widget
from django import forms
from django.forms import ValidationError
from .models import Cliente, Servicio,Equipo, Contrato, Pago



class ClienteForm (forms.ModelForm):
    class Meta:
       model = Cliente  
       fields = '__all__'   

class ServicioForm (forms.ModelForm):
    class Meta:
       model = Servicio  
       fields = '__all__'   

class EquipoForm (forms.ModelForm):
    class Meta:
       model = Equipo  
       fields = '__all__'          

class ContratoForm (forms.ModelForm):
    class Meta:
       model = Contrato  
       fields = '__all__'          

class PagoForm (forms.ModelForm):
    class Meta:
       model = Pago  
       fields = '__all__'   