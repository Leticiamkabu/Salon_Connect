from .views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

app_name = 'service_provider'

urlpatterns = [
    path('',service_provider_view, name = 'service_provider_dashboard'),
    # path('',view_service, name = 'service_view')
]