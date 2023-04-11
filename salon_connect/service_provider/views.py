from django.shortcuts import render, redirect
from .forms import *
from authentication.forms import *
from authentication.models import *
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required


from django.contrib.auth import get_user_model
# Create your views here.
import requests

User = get_user_model()
@login_required
def service_provider_view(request):
    create_service = CreateServiceForm()
    # user = User.objects.get(request.user)
    if request.method == 'POST':
        create_service = CreateService(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            phone_number = request.POST['phone_number'],
            salon_name = request.POST['salon_name'],
            salon_services = request.POST['salon_services'],
            opening_and_closing_time = request.POST['opening_and_closing_time'],
            location = request.POST['location'],
            salon_color = request.POST['salon_color'],
            user = request.user
        )
        image = request.FILES['image']
        create_service.image.save(image.name, image)
        create_service.save()
        messages.success(request,'Service Created')
        
        return redirect('service_provider:service_provider_dashboard')
    
    
    # this displays all the services created 
    services = CreateService.objects.all()
    
    context = {
        
        'create_service': create_service,
        'services': services
        
    }
    
    
    return render(request, 'service_provider/service_provider.html', context)


def view_service(request, user):
    service = CreateService.objects.all()
    
    if service.user == request.user:
        view = Create_service.objects.get(user = request.user)
        
    print(view)
    
    context = {
        
        'service': service,
        
        
    }
    return render(request, 'service_provider/service_provider.html', context)