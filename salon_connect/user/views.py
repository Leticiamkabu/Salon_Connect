from django.shortcuts import render
from service_provider.models import *
# Create your views here.

def user_dashboard_view(request):
    services = CreateService.objects.all()
    # print(services.image.url)
    
    context = {
        'services': services
    }
    
    return render(request, 'user/user_dashboard.html', context)
