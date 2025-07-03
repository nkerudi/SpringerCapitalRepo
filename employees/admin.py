from django.contrib import admin
from .models import Employee, Department 
# Registering Employee, Department models 
admin.site.register(Employee)
admin.site.register(Department)