from django.shortcuts import render, redirect
from .models import *
from .forms import *
# from django.contrib.
# display messages
from django.contrib import messages

# for the login process
from django.contrib.auth import authenticate, login, logout

# decorators to resict access of pages.
from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth import get_user_model
User = get_user_model()
# Create your views here.

# login
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        print(user)

        if user is not None:
            print("yes")
            login(request, user)
            if user.role == "U":
                return redirect('user:user_dashboard' )

            elif user.role == "S":
                return redirect('service_provider:service_provider_dashboard' )

        else:
            print("does not work")

    return render(request, 'login/login.html')




def register_view(request):
    
    if request.method == "POST":
        
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        roles = request.POST['role']
        
        
        print(roles)
        
        if roles == "U":
            user = UserRegistration.objects.create(
            username = username,
            email = email,
            role = roles
            )
            user.set_password(password1)
            user.save()
            
        if roles == "S":
            user = UserRegistration.objects.create(
            username = username,
            email = email,
            role = roles
            )

        
            user.set_password(password1)
            user.save()
        
        return redirect('auth:log-in' )
    else:
        form = RegisterationForm()
    context = {
            'form': form
        }
    
    return render(request, 'register/register.html',context)

def logout_view(request):
    logout(request)
    return redirect('auth:log-in')


# @login_required(login_url = 'log-in')