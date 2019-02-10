from django.shortcuts import render
from django.utils import timezone

from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from .models import Appointment, Service


# Create your views here.

class AppointmentCreate(CreateView):
    model = Appointment
    fields = ['email', 'dni', 'fecha']
    

class ServiceList(ListView):
    model = Service
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
