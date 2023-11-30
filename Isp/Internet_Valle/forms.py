from cProfile import label
from dataclasses import fields
from pyexpat import model
#from tkinter.ttk import Widget
from django import forms
from django.forms import ValidationError
from .models import Cliente, Servicio,Equipo, Contrato, Pago, Adicional, Localidad
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit, HTML
from crispy_forms.layout import Layout, Fieldset, Div, HTML

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
       fields = ['velocidad', 'monto']
       widgets = {
           'velocidad': forms.TextInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'Velocidad'}),
           'monto': forms.TextInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'Monto'}),
       }

class EquipoForm (forms.ModelForm):
    class Meta:
       model = Equipo  
       fields = '__all__'     
       widgets = {
           'nombre': forms.TextInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'Nombre'}),
           'fecha_fin': forms.TextInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'Fecha fin'}),
           'descripcion': forms.TextInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'Descripcion'}),
       }     


class ContratoForm (forms.ModelForm):

    class Meta:
        model = Contrato  
        fields = '__all__'     
        widgets = {
           
           'direccion': forms.TextInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'Direccion'}),
           'fecha_inicio': forms.DateInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'Fecha Inicio','type':'date'}),
           'fecha_fin': forms.DateInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'Fecha Fin','type':'date'}),
          } 
   
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cliente'].queryset = Cliente.objects.all()
        self.fields['servicio'].queryset = Servicio.objects.all()
        self.fields['localidad'].queryset = Localidad.objects.all()
    
        
   
 

       
class PagoForm (forms.ModelForm):
    class Meta:
       model = Pago  
       fields = '__all__'   
       widgets = {
           'contrato': forms.TextInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'Contrato'}),
           'monto_total': forms.TextInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'Monto Total'}),
           'fecha_emision': forms.TextInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'Fecha Emision'}),
           'fecha_vencimiento': forms.TextInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'Fecha Vencimiento'}),
           'fecha_pago': forms.TextInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'Fecha Pago'}),
       }

class AdicionalForm (forms.ModelForm):
    class Meta:
       model = Adicional  
       fields = '__all__' 
       widgets = {
           'monto': forms.TextInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'Monto'}),
           'descripcion': forms.TextInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'Descripcion'}),
        }
    

class LocalidadForm (forms.ModelForm):
    class Meta:
       model = Localidad
       fields = '__all__' 
       widgets = {
           'nombre': forms.TextInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'Nombre'}),
           }
