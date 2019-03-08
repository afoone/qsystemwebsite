from django.db.models import Count
from citas.models import Appointment
from .models import CalendarException
import datetime


def get_occupation(lastmonday, nextmonday, max_appointments_per_slot):
    
        occupations = {}

        occupations['monday'] = list(
                Appointment.objects.all().values('hora').annotate(total=Count('hora')).filter(
                fecha = lastmonday,
                ).order_by('hora'))
        occupations['tuesday'] = list(
                Appointment.objects.all().values('hora').annotate(total=Count('hora')).filter(
                fecha = lastmonday + datetime.timedelta(days=1),
                ))
        occupations['wednesday'] = list(
                Appointment.objects.all().values('hora').annotate(total=Count('hora')).filter(
                fecha = lastmonday + datetime.timedelta(days=2),
                ))
        occupations['thursday'] = list(
                Appointment.objects.all().values('hora').annotate(total=Count('hora')).filter(
                fecha = lastmonday + datetime.timedelta(days=3),
                ))
        occupations['friday'] = list(
                Appointment.objects.all().values('hora').annotate(total=Count('hora')).filter(
                fecha = lastmonday + datetime.timedelta(days=4),
                ))

        print(occupations)

        occupated = {}
        for day in occupations:
                slotting = []
                for slot in occupations[day]:
                        if slot['total'] >= max_appointments_per_slot:  
                                slotting.append(slot['hora'].strftime('%H:%M'))
                occupated[day] = slotting
                

        return occupated



# Devuelve un elemento que para la semana actual dice qué elementos hay que renderizar y cuales no
def get_render_vector(today, week):
        if week > 0:
                return [True, True, True, True, True]
        else:
                
                lastmonday = today - datetime.timedelta(days=today.weekday())
                tuesday = today - datetime.timedelta(days=today.weekday()-1)
                wednesday = today - datetime.timedelta(days=today.weekday()-2)
                thursday = today - datetime.timedelta(days=today.weekday()-3)
                friday = today - datetime.timedelta(days=today.weekday()-4)

                #elementos que dicen si hay que posibillidar o no la reserva
                available_dates=[]
                available_dates.append(lastmonday>today)
                available_dates.append(tuesday>today)
                available_dates.append(wednesday>today)
                available_dates.append(thursday>today)
                available_dates.append(friday>today)

                return available_dates


def get_exceptions_vector(calendar, date_init, date_end):
        result = []
        for single_date in (date_init + datetime.timedelta(n) for n in range(5)):
                objects = CalendarException.objects.filter(date__range=[single_date, single_date]).first()
                if (objects):
                        result.append(False)
                else:
                        result.append(True)
        return result