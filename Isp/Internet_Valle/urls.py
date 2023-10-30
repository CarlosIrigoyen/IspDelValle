from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
 ################### CLIENTE ###################
path('crear/',ClienteCreateView.as_view(), name="ClienteCrear"),
path('modificar/<int:pk>',ClienteUpdateView.as_view(), name="modificarCliente"),
path('Cliente/<int:pk>',ClienteDetailView.as_view(), name="Cliente"),

 ################### Servicio ###################
path('crear/',ServicioCreateView.as_view(), name="ServicioCrear"),
path('modificar/<int:pk>',ServicioUpdateView.as_view(), name="modificarServicio"),
path('Servicio/<int:pk>',ServicioDetailView.as_view(), name="Servicio"),

 ################### Equipo ###################
path('crear/',EquipoCreateView.as_view(), name="EquipoCrear"),
path('modificar/<int:pk>',EquipoUpdateView.as_view(), name="modificarEquipo"),
path('Equipo/<int:pk>',EquipoDetailView.as_view(), name="Equipo"),

 ################### Contrato ###################
path('crear/',ContratoCreateView.as_view(), name="ContratoCrear"),
path('modificar/<int:pk>',ContratoUpdateView.as_view(), name="modificarContrato"),
path('Contrato/<int:pk>',ContratoDetailView.as_view(), name="Contrato"),

 ################### Pago ###################
path('crear/',PagoCreateView.as_view(), name="PagoCrear"),
path('modificar/<int:pk>',PagoUpdateView.as_view(), name="modificarPago"),
path('Pago/<int:pk>',PagoDetailView.as_view(), name="Pago"),

################### Detalle_Pago ###################
path('crear/',Detalle_PagoCreateView.as_view(), name="Detalle_PagoCrear"),
path('modificar/<int:pk>',Detalle_PagoUpdateView.as_view(), name="modificarDetalle_Pago"),
path('Detalle_Pago/<int:pk>',Detalle_PagoDetailView.as_view(), name="Detalle_Pago"),

################### adicionales ###################
path('crear/',adicionalesCreateView.as_view(), name="adicionalesCrear"),
path('modificar/<int:pk>',adicionalesUpdateView.as_view(), name="modificaradicionales"),
path('adicionales/<int:pk>',adicionalesDetailView.as_view(), name="adicionales"),

]