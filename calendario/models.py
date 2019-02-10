from django.db import models
from citas import models as citas_models

# Create your models here.

class CalendarTime(models.Model):
    startTime = models.CharField(max_length = 5, default='09:00')
    endTime = models.CharField(max_length = 5, default = "14:45")

    def get_slots(self):
        # devuelve los slots
        hour_start = int(self.startTime[0:2])
        minutes_start = int(self.startTime[3:5])
        hour_finish = int(self.endTime[0:2])
        minutes_finish = int(self.endTime[3:5])

        slots = []
        hour = hour_start
        minutes = minutes_start
        while hour < hour_finish or minutes < minutes_finish:
            some_slot = {}
            text_hour = ""
            if hour<10:
                text_hour="0"+str(hour)
            else:
                text_hour=str(hour)
            if minutes<10:
                text_min="0"+str(minutes)
            else:
                text_min=str(minutes)
            some_slot['init'] = text_hour+":"+ text_min
            minutes = minutes + 15
            if minutes >= 60:
                minutes = minutes - 60
                hour = hour + 1
            if hour<10:
                text_hour="0"+str(hour)
            else:
                text_hour=str(hour)
            if minutes<10:
                text_min="0"+str(minutes)
            else:
                text_min=str(minutes)
            some_slot['end'] =  text_hour+":"+text_min
            slots.append(some_slot)
                    
        return slots

    def __str__(self):
        return self.startTime + " a " + self.endTime

class CalendarConfig(models.Model):
    time = models.ManyToManyField(CalendarTime)
    service = models.ForeignKey(citas_models.Service, on_delete=models.CASCADE)
    slotSize = models.IntegerField(verbose_name="Tamaño del hueco en minutos", default=15)
    appointmentsPerSlot = models.IntegerField(verbose_name="Máximo número de citas por tramo",  default=1)


    
