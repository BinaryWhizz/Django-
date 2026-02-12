from django.shortcuts import render, redirect

# Create your views here.

def home(request):
    # return HttpResponse("Hello, This is YBalpha home page")
    return render(request, 'website/main.html')

def about(request):
    return render(request, 'alpha/about.html')

def contact(request):
    return render(request, 'alpha/contact.html')