from django.shortcuts import render
from django.views.generic import ListView,CreateView
from employeeApp.models import EmployeeData

# Create your views here.
def index(request):
    return render(request,'index.html')

class EmployeeList(ListView):
    context_object_name = 'Employeelist'
    model = EmployeeData

class EmployeeCreateView(CreateView):
    model = EmployeeData
    fields = '__all__'