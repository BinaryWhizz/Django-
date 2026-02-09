from django.shortcuts import render
from .models import BinaryVarity, Student
from django.shortcuts import get_object_or_404
from .forms import BinaryVarityForm

# Create your views here.

def all_binary(request):
    binaries = BinaryVarity.objects.all
    return render(request, 'Binary/all_binary.html', {'binaries': binaries}) 

def binary_descp(request, binary_id):
    binary = get_object_or_404(BinaryVarity, pk=binary_id)     # BinaryVarity from models.py
    return render(request, 'Binary/binary_descriptions.html', {'binary':binary}) 

def binary_student(request):
    students = None   # why need this variable ? - when we submit form, need to pass this to frontend 

    if request.method == 'POST' : 
        form = BinaryVarityForm(request.POST)

        if form.is_valid():
            binaryVarity = form.cleaned_data['binary_varity']  # binary_varity : from forms.py line 6 
            students = Student.objects.filter(binary_varieties = binaryVarity) # binary_Varities : from models.py line 45
            
    else:
        form = BinaryVarityForm()

    return render(request, 'Binary/binary_Students.html', {'students':students, 'form': form}) # sending form & students to frontend 

