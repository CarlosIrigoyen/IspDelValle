from cProfile import label
from dataclasses import fields
from pyexpat import model
#from tkinter.ttk import Widget
from django import forms
from django.forms import ValidationError
from .models import Cliente



class ClienteForm (forms.ModelForm):
    class Meta:
       model = Cliente  
       fields = '__all__'   
    