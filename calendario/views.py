from django.shortcuts import render
from qsystemwebsite import settings
from citas.models import Service
from .models import CalendarConfig
import datetime

# Create your views here.
def calendar(request, service_id, actual_week):
    s = Service.objects.filter(serviceID=service_id)
    actual_calendar = CalendarConfig.objects.filter(service = s.first().id)
    today = datetime.datetime.now()

    if actual_week > 0:
        today = today + datetime.timedelta(days=-today.weekday(), weeks=actual_week)
    
    print (today)
    nextmonday = today + datetime.timedelta(days=-today.weekday(), weeks=1)
    lastmonday = today - datetime.timedelta(days=today.weekday())
    actual_service = s.first()    
    available_dates = get_render_vector(today, actual_week)

    print(available_dates)

    context = {
        'company_name': "Territorial de Valencia",
        'service_name': actual_service.description,
        'service_id': actual_service.id,
        'slots': actual_calendar.first().time.first().get_slots(),
        'days': settings.DAYS_OF_WEEK,
        'date_from': lastmonday,
        'date_to': nextmonday,
        'now': today,
        "available_dates":available_dates,
        'weeks_in_advance': actual_service.weeks_in_advance,
        'actual_week': actual_week,

    }
    return render(request, 'calendario/calendar.html', context)






#################################################################
###### NO VISTAS - MÉTODOS DE OTRA COSA
#################################################################




# Devuelve un elemento que para la semana actual dice qué elementos hay que renderizar y cuales no
def get_render_vector(today, week):
    if week > 0:
        return [True, True, True, True, True]
    else:
        lastmonday = today - datetime.timedelta(days=today.weekday())
        thursday = today - datetime.timedelta(days=today.weekday())
        wednesday= today - datetime.timedelta(days=today.weekday())
        thursday= today - datetime.timedelta(days=today.weekday())
        friday= today - datetime.timedelta(days=today.weekday())

        #elementos que dicen si hay que posibillidar o no la reserva
        available_dates=[]
        available_dates.append(lastmonday>today)
        available_dates.append(thursday>today)
        available_dates.append(wednesday>today)
        available_dates.append(thursday>today)
        available_dates.append(friday>today)

        return available_dates

