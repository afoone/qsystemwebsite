from django.contrib import admin
from .models import CalendarConfig, CalendarTime

# Register your models here.
admin.site.register(CalendarConfig)
admin.site.register(CalendarTime)

