from django.shortcuts import render, redirect

from .forms import *

# display messages
from django.contrib import messages

# for the login process
from django.contrib.auth import authenticate, login, logout

# decorators to resict access of pages.
from django.contrib.auth.decorators import login_required
# Create your views here.

# login
def login_view(request):
    if request.method == 'POST':
       username = request.POST.get('username')
       password = request.POST.get('password')
       
       user = authenticate(request, username=username, password=password)
       
       if user is not None:
           login(request, user)
           return redirect('log-in')
       else:
           messages.info(request, 'Username or Password is not valid ')
       
    return render(request, 'login/login.html')


# register
# def register_view(request):
#     if request.user.is_authenticated:
#         messages.success(request, 'Account was creates successfully')
#         return redirect('')
#     else:
#         form = RegisterationForm()
        
#         if request.method == "POST":
#             form =  RegisterationForm(request.POST)
#             if form.is_valid():
#                 form.save()
#                 login(request, form.save())
#                 user = form.cleaned_data.get('username')this gets the username when created
#                 messages.success(request, 'Account was creates successfully' + user)  this displaces a sucess message when account has been created.
#                 return redirect('auth:log-in')
            
                
#         context = {
#             'form': form
#         }
        
#         return render(request, 'register/register.html',context)

def register_view(request):
    form = RegisterationForm()
    if request.method == "POST":
            form =  RegisterationForm(request.POST)
            if form.is_valid():
                form.save()
                return render(request, 'login/login.html')
            else:
                messages.error(request, 'Account was not created')
    else:
        form = RegisterationForm()
    context = {
            'form': form
        }
    
    return render(request, 'register/register.html',context)

def logout_view(request):
    logout(request)
    return redirect('log-in')


# @login_required(login_url = 'log-in')