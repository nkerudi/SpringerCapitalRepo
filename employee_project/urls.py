"""
URL configuration for employee_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path 
from rest_framework import permissions 
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import (
    TokenObtainPairView, 
    TokenRefreshView
)
from employees.views import employees_per_department, monthly_attendance 
from employees.views import employees_per_department
from attendance.views import monthly_attendance 
from django.core.management import call_command
from django.http import JsonResponse


schema_view = get_schema_view(
    openapi.Info(
        title= "Employee Management API", 
        default_version="v1", 
        description="API documentation for Employee Management System", 
        contact = openapi.Contact(email= 'nikithakerudi@gmail.com')
    ), 
    public = True, 
    permission_classes=[permissions.AllowAny],
    authentication_classes=[]
)


def trigger_migrate(request):
    call_command('migrate')
    return JsonResponse({'message': 'Migrations applied successfully'})

def trigger_seed(request):
    call_command('seed_data')
    return JsonResponse({'message': 'Seed data inserted successfully'})

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/employees/', include('employees.urls')),
    path('api/attendance/', include('attendance.urls')),
    path('api/performance/', include('performance.urls')),
    path('chart/employees-per-department/', employees_per_department),
    path('chart/monthly-attendance/', monthly_attendance),
    path('trigger-migrate/', trigger_migrate),
    path('trigger-seed/', trigger_seed),
]

