from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import filters
from .models import Employee, Department
from .serializers import EmployeeSerializer, DepartmentSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .filters import EmployeeFilter
from django.db.models import Count
from employees.models import Employee
from attendance.models import Attendance
from django.db.models.functions import TruncMonth
from django.http import HttpResponse
from django.core.management import call_command


# Create your views here.
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class= EmployeeSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = EmployeeFilter
    search_fields = ['first_name', 'last_name', 'email']
    ordering_fields = ['first_name', 'last_name', 'date_joined']
    ordering = ['date_joined']

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class= DepartmentSerializer
    


def employees_per_department(request):
    return render(request, 'charts.html', {
        'chart_title': 'Employee Attendance by Department',
        'labels': ['HR', 'IT', 'Finance'],
        'counts': [10, 15, 7]
    })

def monthly_attendance(request):
    data = (
        Attendance.objects
        .annotate(month=TruncMonth('date'))
        .values('month')
        .annotate(count=Count('id'))
        .order_by('month')
    )
    labels = [item['month'].strftime('%B %Y') for item in data]
    counts = [item['count'] for item in data]

    return render(request, 'charts.html', {
        'labels': labels,
        'counts': counts,
        'chart_title': 'Monthly Attendance Overview'
    })

def trigger_seed(request):
    call_command("seed_data")
    return HttpResponse("Seeding complete.")
