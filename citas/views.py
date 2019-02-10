from django.shortcuts import render
from django.utils import timezone
from django.urls import reverse

from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from .models import Appointment, Service
from .forms import CreateAppointmentForm
import datetime


# Create your views here.

class AppointmentCreate(CreateView):
    model = Appointment
    form_class = CreateAppointmentForm
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(self.kwargs)
        context["date"] = self.kwargs['cita_date']
        context['time'] = self.kwargs['cita_time']
        return context
    def get_success_url(self):
        return reverse('service-list')
    def get_initial(self):
        fill_date = datetime.datetime.strptime(self.kwargs['cita_date'], "%d%m%y").date()
        fill_hour = datetime.datetime.strptime(self.kwargs['cita_time'], "%H:%M").time()
        
        print(fill_date)
        return { 'fecha': fill_date, 'hora':fill_hour}

    

class ServiceList(ListView):
    model = Service
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
