from cProfile import label
from dataclasses import fields
from pyexpat import model
#from tkinter.ttk import Widget
from django import forms
from django.forms import ValidationError
from .models import Cliente, Servicio,Equipo, Contrato, Pago, Adicional



class ClienteForm (forms.ModelForm):
    class Meta:
       model = Cliente
       fields = ['nombre', 'apellido', 'dni', 'telefono', 'mail']
       widgets = {
           'nombre': forms.TextInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'Nombre'}),
           'apellido': forms.TextInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'Apellido'}),
           'dni': forms.TextInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'Documento'}),
           'telefono': forms.TextInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'Telefono'}),
           'mail': forms.TextInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'Email'}),
       }

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

class AdicionalForm (forms.ModelForm):
    class Meta:
       model = Adicional  
       fields = '__all__'   