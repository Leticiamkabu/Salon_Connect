from django.shortcuts import render

# Create your views here.

def user_dashboard_view(request):
    return render(request, 'user/user_dashboard.html')
