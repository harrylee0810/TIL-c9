from django.shortcuts import render
from .models import Studentc

# Create your views here.
def new(request):
    return render(request, 'new.html')
    
def create(request):
    name = request.GET.get('name')
    age = request.GET.get('age')
    uni = request.GET.get('uni')
    
    student = Student(name=name, age=age, uni=uni)
    student.save()
    
    return render(request, 'create.html', {'student':student})

def index(request):
    
    students = Student.objects.all()
    
    return render(request, 'index.html', {'students':students})