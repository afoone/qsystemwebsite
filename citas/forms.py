from django import forms

class CreateAppointmentForm(forms.Form):
    dni = forms.CharField(label = "Nombre", required = True, widget=forms.TextInput(attrs={'class': 'form-control'}), min_length=3, max_length=100)
    email = forms.EmailField(label = "Correo-e", required = True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    fecha = forms.DateTimeField(verbose_name="Fecha de la cita", widget=forms.DateInput(attrs={'class': 'form-control'}))
   