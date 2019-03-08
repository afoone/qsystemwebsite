from django.contrib import admin
from .models import CalendarConfig, CalendarTime, CalendarException

# Register your models here.
admin.site.register(CalendarConfig)
admin.site.register(CalendarTime)
admin.site.register(CalendarException)



