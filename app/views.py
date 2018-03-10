from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Service

def Home(request):
    services = Service.objects.all()
    return render(request, 'app/index.html', {'services':services})



    
# Create your views here.
# def index(request):
#     return render(request, 'app/index.html')