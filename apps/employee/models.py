from django.db import models

from employee_intern.custom_models import DateTimeModel


# Create your models here.

class Employee(DateTimeModel):
    employee_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30,null=True)
    last_name = models.CharField(max_length=30,null=True)
    email = models.EmailField(unique=True,null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    hire_date = models.DateField()
    position = models.CharField(max_length=50,null=True)
    department = models.CharField(max_length=50,null=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2,null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"