from .views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

app_name = 'home'

urlpatterns = [
    path('', home_view, name = "index"),
]