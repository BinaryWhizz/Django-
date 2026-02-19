from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .models import Enquiry


# Create your views here.

def home(request):
    # return HttpResponse("Hello, This is YBalpha home page")
    return render(request, 'website/main.html')

def about(request):
    return render(request, 'alpha/about.html')

def contact(request):
    return render(request, 'alpha/contact.html')

def material(request):
    return render(request, 'alpha/material.html')

def interior(request):
    return render(request, 'alpha/interior.html')

def manpower(request):
    return render(request, 'alpha/manpower.html')

def civil(request):
    return render(request, 'alpha/civil.html')

def services(request):
    return render(request, 'alpha/services.html')