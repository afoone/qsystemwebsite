from django.shortcuts import render
from qsystemwebsite import settings
from citas.models import Service, Appointment
from .models import CalendarConfig
from .services import get_occupation, get_render_vector
import datetime

# Create your views here.
def calendar(request, service_id, actual_week):
    s = Service.objects.filter(serviceID=service_id)
    actual_calendar = CalendarConfig.objects.filter(service = s.first().id).first()
    today = datetime.datetime.now()

    if actual_week > 0:
        today = today + datetime.timedelta(days=-today.weekday(), weeks=actual_week)
    
    print (today)
    nextmonday = today + datetime.timedelta(days=-today.weekday(), weeks=1)
    lastmonday = today - datetime.timedelta(days=today.weekday())
    actual_service = s.first()    
    available_dates = get_render_vector(today, actual_week)

    
    context = {
        'company_name': "Territorial de Valencia",
        'service_name': actual_service.description,
        'service_id': actual_service.id,
        'slots': actual_calendar.time.first().get_slots(),
        'days': settings.DAYS_OF_WEEK,
        'date_from': lastmonday,
        'date_to': nextmonday,
        'now': today,
        "available_dates":available_dates,
        'weeks_in_advance': actual_service.weeks_in_advance,
        'actual_week': actual_week,
        'occupation':get_occupation(lastmonday, nextmonday, actual_calendar.appointmentsPerSlot),

    }
    return render(request, 'calendario/calendar.html', context)






