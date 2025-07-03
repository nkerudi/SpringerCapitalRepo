import django_filters
from .models import Employee 

#Filtering class 
class EmployeeFilter(django_filters.FilterSet):
    date_joined = django_filters.DateFilter(field_name="date_of_joining", lookup_expr='exact')
    department = django_filters.CharFilter(field_name="department__name", lookup_expr='icontains')

    class Meta:
        model = Employee
        fields = ['date_joined', 'department']

