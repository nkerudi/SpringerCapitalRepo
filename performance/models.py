from django.db import models
from datetime import date 

# Performance Model
class Performance(models.Model):
    employee = models.ForeignKey('employees.Employee', on_delete=models.CASCADE)
    rating = models.IntegerField()
    date = models.DateField(default =date.today)
