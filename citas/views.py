from django.shortcuts import render
from django.utils import timezone
from django.urls import reverse, reverse_lazy
from django.core.mail import send_mail


from django.views.generic.edit import CreateView
from django.views.generic import DetailView, DeleteView
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
        context["date"] = self.kwargs['cita_date']
        context['time'] = self.kwargs['cita_time']
        return context
    def get_success_url(self):
        return reverse('appointment-detail', kwargs={'pk': self.object.id})
    def get_initial(self):
        fill_date = datetime.datetime.strptime(self.kwargs['cita_date'], "%d%m%y").date()
        fill_hour = datetime.datetime.strptime(self.kwargs['cita_time'], "%H:%M").time()
        fill_service_id = self.kwargs['service_id']
        return { 'fecha': fill_date, 'hora':fill_hour, 'service_id': fill_service_id}
    def form_valid(self, form):
        response = super(AppointmentCreate, self).form_valid(form)
        body = "Su cita para el DNI "+self.object.dni+" está CONFIRMADA con los siguientes datos:\n<br/>"
        body+= "\n Fecha:"+self.object.fecha.strftime('%d/%m/%Y')+"<br/>"
        body+= "\n Hora:"+self.object.hora.strftime('%H:%M')+"<br/>"
        body+= """<br/><br/>
        Cuando llegue a la dirección territorial ha de dirigirse al kiosco y en el botón <br/>
        "cita por Internet" deberá introducir el mismo número de DNI que ha indicado en <br/>
        la reserva de la cita, sin letra.<br/><br/>

        Gracias por usar el servicio de cita por Internet.        <br/><br/>
        
        Este es un mensaje automático, por favor no responda a este correo.        <br/><br/>

        """
        body+= "Para anular la cita siga o copie el siguiente enlace en el navegador:\n<br/>"
        url_to_delete = "http://territorial-valencia.gestiondecolasdeespera.com/"+reverse('appointment-delete',kwargs={"pk":self.object.id, "dni":self.object.dni})
        body+= "<a href='"+url_to_delete+"'>"+url_to_delete+"</a><br/>"
        
        send_mail(subject="Su cita para la Dirección Territorial",message = body, html_message=body, from_email= "territorial@gestiondecolasdeespera.com", recipient_list=(self.object.email,) )

        return response

class AppointmentView(DetailView):
    model = Appointment
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class AppointmentDelete(DeleteView):
    model = Appointment
    success_url = reverse_lazy('service-list')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["dni"] = self.kwargs['dni']
        return context
    

class ServiceList(ListView):
    model = Service
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
