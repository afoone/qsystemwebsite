from django.db import models

# Clase para citas
class Appointment(models.Model):
    dni = models.CharField(verbose_name="DNI o NIE (Sin letra)", max_length = 15)
    email = models.EmailField(verbose_name="Dirección de correo donde se enviará la confirmación", max_length=254)
    fecha = models.DateField(verbose_name="Fecha de la cita")
    hora = models.TimeField(verbose_name="Hora de la cita", default='09:00')
    service_id = models.IntegerField(verbose_name="Número de servicio en el sistema", default=2)
    def __str__(self):
        return self.dni
    


class Service(models.Model):
    serviceID = models.BigIntegerField(verbose_name="Número de servicio en el sistema")
    description = models.TextField(verbose_name="Descripción")
    weeks_in_advance = models.IntegerField (verbose_name="Semanas en las que se puede reservar con antelación", default=2)
    def __str__(self):
        return self.description