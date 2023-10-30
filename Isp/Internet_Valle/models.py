from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    dni = models.PositiveSmallIntegerField(max_length=8,unique=True)
    telefono = models.CharField(max_length=11)
    mail = models.EmailField(max_length = 254) 

class Servicio (models.Model):
    velocidad = models.IntegerField(max_length=4)
    fecha_fin = models.DateField(blank=True)
    monto = models.DecimalField(help_text="costo del servicio", max_digits=10, decimal_places=2)

class Equipo (models.Model):
    nombre = models.CharField(max_length=40)
    fecha_fin = models.DateField(blank=True)
    descripcion = models.CharField(max_length=500)

class Contrato (models.Model):
    cliente = models.ForeignKey(Cliente, related_name="contrato")
    servicio = models.ForeignKey(Servicio)
    direccion = models.CharField(max_length=40)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(blank=True)
    fecha_desconexion = models.DateField(blank=True)

class Pago (models.Model):
    contrato = models.ForeignKey(Contrato, related_name="pago")
    monto_total =  models.DecimalField(help_text="monto total del pago", max_digits=10, decimal_places=2)
    fecha_emision = models.DateField()
    fecha_vencimiento = models.DateField(blank=True)
    fecha_pago = models.DateField(blank=True)

class Detalle_Pago (models.Model):
    pago = models.ForeignKey(Pago, related_name="Detalle de pago")
    renglon = models.CharField(max_length=500)
    costo =  models.DecimalField(help_text="costo", max_digits=10, decimal_places=2)

class adicionales (models.Model):
    monto =  models.DecimalField(help_text="monto del servicio", max_digits=10, decimal_places=2)
    descripcion = models.CharField(max_length=500)

