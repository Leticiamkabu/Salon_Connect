from django.shortcuts import render
from .models import *
# Create your views here.

def home_view(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        messages = Message(
            name = name,
            email = email,
            message = message
        )

        messages.save()

    return render(request,'home/index.html')