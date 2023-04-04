from django.shortcuts import render, redirect
from .forms import *
from authentication.forms import *
from authentication.models import *
from django.contrib import messages


from django.contrib.auth import get_user_model
# Create your views here.
import requests

User = get_user_model()

def service_provider_view(request,user_id):
    create_service = CreateServiceForm()
    user = UserRegistration.objects.get(pk=user_id)
    if request.method == 'POST':
        create_service = CreateService(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            phone_number = request.POST['phone_number'],
            salon_name = request.POST['salon_name'],
            salon_services = request.POST['salon_services'],
            opening_and_closing_time = request.POST['opening_and_closing_time'],
            location = request.POST['location'],
            salon_color = request.POST['salon_color']
        )
        image = request.FILES['image']
        create_service.image.save(image.name, image)
        create_service.save()
        messages.success(request,'Service Created')
        redirect('service_provider:service_provider_dashboard')
        
        
    context = {
        
        'create_service': create_service,
        
    }
    
    
    return render(request, 'service_provider/service_provider.html', context)
