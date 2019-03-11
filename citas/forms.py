from django import forms
from .models import Appointment
from datetime import datetime

class CreateAppointmentForm(forms.ModelForm):
    dni = forms.CharField(label = "DNI / NIE (SIN LETRA)", required = True, widget=forms.TextInput(attrs={'class': 'form-control'}), min_length=3, max_length=100)
    email = forms.EmailField(label = "Correo-e", required = True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    fecha = forms.DateField(required = True, widget=forms.HiddenInput())
    hora = forms.TimeField(required = True, widget=forms.HiddenInput())
    service_id = forms.IntegerField(required = True, widget=forms.HiddenInput())

    class Meta:
        model = Appointment
        fields = ('dni', 'email', 'fecha', 'hora', 'service_id')

    def clean_email(self):
        #print("Comprobando si ya tenía una cita")
        form_email = self.cleaned_data.get('email')
        appointment_in_the_future = Appointment.objects.filter(
            email=form_email,
            fecha__gt = datetime.now(),
            )
        existing = appointment_in_the_future.exists()

        if existing:
            raise forms.ValidationError(u"Ya dispone una cita el "+ appointment_in_the_future.first().fecha.strftime('%d-%m-%Y')+" con este correo electrónico. Para anular dicha la cita revise el correo electrónico de confirmación.")


        return form_email


    def clean_dni(self):
        #Comprobando si son sólo números
        form_dni = self.cleaned_data.get('dni')
        if not form_dni.isdigit():
            raise forms.ValidationError(u"Por favor, ingrese sólo los dígitos del documento")
        appointment_in_the_future = Appointment.objects.filter(
            dni=form_dni,
            fecha__gt = datetime.now(),
            )
        existing = appointment_in_the_future.exists()
        if existing:
            raise forms.ValidationError(u"Ya dispone una cita el "+ appointment_in_the_future.first().fecha.strftime('%d-%m-%Y')+" con este Documento. Para anular dicha la cita revise el correo electrónico de confirmación.")
        return form_dni
   