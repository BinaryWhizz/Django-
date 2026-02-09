from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    # return HttpResponse("Hello, Home Page")
    # return render(request, 'index.html')    # Shows error , so correct path should be --->
    return render(request, 'website/index.html') 

def about(request):
    return HttpResponse("Hello, About Page")

def contact(request):
    return HttpResponse("Hello, Contact Page")

