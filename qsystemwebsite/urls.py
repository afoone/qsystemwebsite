"""qsystemwebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include, re_path
from core import views
from django.conf import settings
from citas import urls as citasurls
from citas.views import ServiceList
from calendario import urls as calendar_urls
from django.views.generic import RedirectView




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ServiceList.as_view(), name = "home"),
    path('appointment/', include(citasurls)),
    path('calendar/', include(calendar_urls)),
    re_path(r'^api-auth/', include('rest_framework.urls')),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)