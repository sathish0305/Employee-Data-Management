from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView,CreateView,UpdateView,DeleteView,DetailView
from employeeApp.models import EmployeeData
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import redirect

# Create your views here.
def index(request):
    return render(request,'index.html')

class EmployeeList(ListView):
    context_object_name = 'Employeelist'
    model = EmployeeData
    ordering=['employee_id']
    paginate_by = 8

class EmployeeCreateView(CreateView):
    model = EmployeeData
    fields = '__all__'

    def form_valid(self, form):
        # Check if the name already exists in the database
        employee_id = form.cleaned_data['employee_id']
        phone_number = form.cleaned_data['phone']
        if len(str(phone_number)) != 10:
            form.add_error('phone','Enter Valid Phone Number')
            return self.form_invalid(form)
        
        if EmployeeData.objects.filter(employee_id=employee_id).exists():
            form.add_error('employee_id', 'This EmployeeId already exists.')
            return self.form_invalid(form)
        return super().form_valid(form)

class EmployeeUpdateView(UpdateView):
    model = EmployeeData
    fields = '__all__'

class EmployeeDeleteView(DeleteView):
    context_object_name = 'EmployeeDelete'
    model = EmployeeData
    success_url = reverse_lazy('empapp:list')

class EmployeeDetailView(DetailView):
    context_object_name = 'employeeDetail'
    model = EmployeeData

def user_login(request):
    return render(request,'login.html')