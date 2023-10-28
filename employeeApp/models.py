from django.db import models
from django.urls import reverse

# Create your models here.
class EmployeeData(models.Model):
    employee_id = models.CharField(max_length=10)
    employee_name = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    email = models.EmailField()
    phone = models.IntegerField()
    address = models.CharField(max_length=200)
    hire_date =  models.DateField()
    position = models.CharField(max_length=200)

    def __str__(self):
        return self.employee_name
    
    def get_absolute_url(self):
        return reverse('empapp:list')