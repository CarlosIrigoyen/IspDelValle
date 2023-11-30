from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    dni = models.PositiveSmallIntegerField(unique=True)
    telefono = models.CharField(max_length=11)
    mail = models.EmailField(max_length = 254) 

    def __str__(self):
        return f"{self.nombre}, {self.apellido}"

class Servicio (models.Model):
    velocidad = models.IntegerField()
    fecha_fin = models.DateField(blank=True,null=True),
    monto = models.DecimalField(help_text="costo del servicio", max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.velocidad}"

class Equipo (models.Model):
    nombre = models.CharField(max_length=40)
    fecha_fin = models.DateField(blank=True)
    descripcion = models.CharField(max_length=500)

class Localidad (models.Model): 
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre}"

class Contrato (models.Model):
    cliente = models.ForeignKey(Cliente, related_name="contrato",on_delete=models.CASCADE)
    servicio = models.ForeignKey(Servicio,on_delete=models.CASCADE)
    direccion = models.CharField(max_length=40)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(blank=True)
    fecha_desconexion = models.DateField(blank=True, null=True)
    localidad = models.ForeignKey(Localidad, related_name="localidad", on_delete=models.CASCADE)

    
    
class Pago (models.Model):
    contrato = models.ForeignKey(Contrato, related_name="pago",on_delete=models.CASCADE)
    monto_total =  models.DecimalField(help_text="monto total del pago", max_digits=10, decimal_places=2)
    fecha_emision = models.DateField()
    fecha_vencimiento = models.DateField(blank=True)
    fecha_pago = models.DateField(blank=True)

class Adicional (models.Model):
    monto =  models.DecimalField(help_text="monto del servicio", max_digits=10, decimal_places=2)
    descripcion = models.CharField(max_length=500)

class Detalle_Pago (models.Model):
    pago = models.ForeignKey(Pago, related_name="DetalleDePago",on_delete=models.CASCADE)
    renglon = models.CharField(max_length=500)
    costo =  models.DecimalField(help_text="costo", max_digits=10, decimal_places=2)
    adicional = models.ForeignKey(Adicional, null=True, blank=True, on_delete=models.CASCADE )






