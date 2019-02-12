"""qsystemwebsite URL Configuration

Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from . import views

urlpatterns = [
    path('<int:pk>/', views.AppointmentView.as_view(), name = 'appointment-detail'),
    path('create/<cita_time>/<cita_date>/', views.AppointmentCreate.as_view(), name = "appointment-create"),
    path('', views.ServiceList.as_view(), name = "service-list"),
]