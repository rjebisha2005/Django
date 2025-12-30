from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee
# from.models import jebii
# from myapp.models import Employee
# from .models import students
from .models import Student_Signals

# Create your views here.
def home(request):
    return HttpResponse('Welcome to django...')

# Employee.objects.create(name = "jebi",age = 20 )
#students.objects.create(name = "naveen",age = 23,mark = 67)

# jebii.objects.create(name = "akshuu",age = 20,mark = 89)
# # 

#signals value intrested:

Student_Signals.objects.create(name = "naveen", age = 23)

Student_Signals.objects.create(name = "jebi", age = 20)


