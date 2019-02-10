from django.shortcuts import render, HttpResponse
from qsystemwebsite import settings
from calendario import models

# Create your views here.

def home(request):
    context = {
        'name': "Territorial de Valencia",
        'slots': [
            { 'init': '09:00', 'end': '09:15'},
            { 'init': '09:15', 'end': '09:30'},
            { 'init': '09:30', 'end': '09:45'},
            { 'init': '09:45', 'end': '10:00'},
        ],
        'days': settings.DAYS_OF_WEEK,
    }
    return render(request, 'core/index.html', context)



