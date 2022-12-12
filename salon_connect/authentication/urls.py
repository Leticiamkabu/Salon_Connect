from django.contrib import admin
from django.urls import path
from .views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


app_name = 'auth'

urlpatterns = [
    path('login/',login_view, name = "log-in" ),
    path('register/',register_view, name= "reg"),
    path('logout/',logout_view, name = "log-out" ),
]