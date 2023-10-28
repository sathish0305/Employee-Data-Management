from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView,CreateView,UpdateView
from employeeApp.models import EmployeeData

# Create your views here.
def index(request):
    return render(request,'index.html')

class EmployeeList(ListView):
    context_object_name = 'Employeelist'
    model = EmployeeData
    ordering=['employee_id']

class EmployeeCreateView(CreateView):
    model = EmployeeData
    fields = '__all__'

class EmployeeUpdateView(UpdateView):
    model = EmployeeData
    fields = '__all__'