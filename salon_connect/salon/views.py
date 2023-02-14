from django.shortcuts import render

# Create your views here.
def click(request):
    
    return render(request, '/salons/shell.html')