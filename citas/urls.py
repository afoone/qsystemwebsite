from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from . import views
from .models import Appointment, Service
from rest_framework import serializers, viewsets, routers
import datetime


# Serializers define the API representation.
class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ('dni', 'fecha', 'hora', 'email', 'service_id')

# ViewSets define the view behavior.
class AppointmentViewSet(viewsets.ModelViewSet):
    print(datetime.datetime.now())
    #queryset = Appointment.objects.all()
    queryset = Appointment.objects.filter(fecha = datetime.datetime.now() )
    serializer_class = AppointmentSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'appointments', AppointmentViewSet)



urlpatterns = [
    path('api/', include(router.urls)),
    path('<int:pk>/', views.AppointmentView.as_view(), name = 'appointment-detail'),
    path('<int:pk>/<dni>/delete/', views.AppointmentDelete.as_view(), name = 'appointment-delete'),
    path('create/<service_id>/<cita_time>/<cita_date>/', views.AppointmentCreate.as_view(), name = "appointment-create"),
    path('', views.ServiceList.as_view(), name = "service-list"),
]