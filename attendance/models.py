from django.db import models

# Attendance model 
class Attendance(models.Model):
    STATUS_CHOICES = [
        ("Present", "Present"),
        ("Absent", "Absent"), 
        ("Late", "Late") 

    ]
    employee = models.ForeignKey('employees.Employee', on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10, choices = STATUS_CHOICES)
