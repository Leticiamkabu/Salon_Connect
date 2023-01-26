from .views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path


app_name = 'user'

urlpatterns = [
    path('',user_dashboard_view, name = "user_dashboard" )
]