from django.db.models import Count
from citas.models import Appointment
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
        print("max pwer slot")
        print(max_appointments_per_slot)
        for day in occupations:
                slotting = []
                for slot in occupations[day]:
                        print(day)
                        print(slot['total'])
                        if slot['total'] >= max_appointments_per_slot:  
                                print('total')
                                print(slot['total'])
                                slotting.append(slot['hora'].strftime('%H:%M'))
                occupated[day] = slotting
                

        return occupated



# Devuelve un elemento que para la semana actual dice qué elementos hay que renderizar y cuales no
def get_render_vector(today, week):
        print("render vector, week")
        print(week)
        if week > 0:
                return [True, True, True, True, True]
        else:
                
                lastmonday = today - datetime.timedelta(days=today.weekday())
                print (lastmonday)
                tuesday = today - datetime.timedelta(days=today.weekday()-1)
                print(tuesday)
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