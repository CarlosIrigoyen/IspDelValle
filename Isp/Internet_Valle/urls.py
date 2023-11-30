
from django.urls import path, include
from .views import *

urlpatterns =[
 ################### CLIENTE ###################
    path('crearCliente/',ClienteCreateView.as_view(), name="ClienteCrear"),
    path('modificar/<int:pk>',ClienteUpdateView.as_view(), name="modificarCliente"),
    path('clienteListar/',ClienteListar.as_view(),name="ClienteListar"),

 ################### Servicio ###################
    path('crearServicio/',ServicioCreateView.as_view(), name="ServicioCrear"),
    path('modificar/<int:pk>',ServicioUpdateView.as_view(), name="modificarServicio"),
    path('Servicio/<int:pk>',ServicioDetailView.as_view(), name="Servicio"),
    path('ServicioListar/',ServicioListar.as_view(),name="ServicioListar"),

 ################### Equipo ###################
    path('crearEquipo/',EquipoCreateView.as_view(), name="EquipoCrear"),
    path('modificar/<int:pk>',EquipoUpdateView.as_view(), name="modificarEquipo"),
    path('Equipo/<int:pk>',EquipoDetailView.as_view(), name="Equipo"),
    path('EquipoListar/',EquipoListar.as_view(),name="EquipoListar"),

 ################### Contrato ###################
    path('crearContrato/',ContratoCreateView.as_view(), name="ContratoCrear"),
    path('modificar/<int:pk>',ContratoUpdateView.as_view(), name="modificarContrato"),
    path('Contrato/<int:pk>',ContratoDetailView.as_view(), name="Contrato"),
    path('ContratoListar/',ContratoListar.as_view(),name="ContratoListar"),
 ################### Pago ###################
    path('crearPago/',PagoCreateView.as_view(), name="PagoCrear"),
    path('modificar/<int:pk>',PagoUpdateView.as_view(), name="modificarPago"),
    path('Pago/<int:pk>',PagoDetailView.as_view(), name="Pago"),

################### Detalle_Pago ###################
    path('crearDetallePago/',Detalle_PagoCreateView.as_view(), name="Detalle_PagoCrear"),
    path('modificar/<int:pk>',Detalle_PagoUpdateView.as_view(), name="modificarDetalle_Pago"),
    path('Detalle_Pago/<int:pk>',Detalle_PagoDetailView.as_view(), name="Detalle_Pago"),

################### Adicional ###################
    path('crearAdicional/',AdicionalCreateView.as_view(), name="adicionalCrear"),
    path('modificar/<int:pk>',AdicionalUpdateView.as_view(), name="modificaradicionales"),
    path('adicional/<int:pk>',AdicionalDetailView.as_view(), name="adicional"),
################### Localidad ###################
    path('crearLocalidad/',LocalidadCreateView.as_view(), name="localidadCrear"),
    path('LocalidadListar/',LocalidadListar.as_view(),name="LocalidadListar"),
]