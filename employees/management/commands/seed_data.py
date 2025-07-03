from django.core.management.base import BaseCommand
from faker import Faker 
import random 
from employees.models import Employee, Department 
from attendance.models import Attendance
from performance.models import Performance 
from datetime import timedelta, date 

faker = Faker()

#command class 
class Command(BaseCommand):
    help_message = 'Seed database with fake data'
    #handle old data 
    def handle(self, *args, **kwargs):
        #clear the old data 
        Performance.objects.all().delete()
        Attendance.objects.all().delete()
        Department.objects.all().delete()
        Employee.objects.all().delete()

        self.stdout.write(self.style.WARNING('Old data was deleted.'))

        #Create Departments 
        departments = []
        department_names = ['HR', 'Engineering', 'Marketing', 'Sales', 'Support']
        for name in department_names:
            dept = Department.objects.create(name=name)
            departments.append(dept)
        self.stdout.write(self.style.SUCCESS(f"Created {len(departments)} departments!"))

        #Create Employees 
        employees = []
        for _ in range(50):
            emp = Employee.objects.create(
                name = faker.name(), 
                email = faker.free_email(), 
                phone = faker.phone_number(), 
                address = faker.address(),
                date_of_joining=faker.date_between(start_date='-3y', end_date='today'), 
                department = random.choice(departments)    
            )
            employees.append(emp)
        self.stdout.write(self.style.SUCCESS(f"Created {len(employees)} employees!"))

        #Create Attendance Records 
        for emp in employees:
            for i in range(10):
                Attendance.objects.create(
                    employee= emp, 
                    date = date.today() - timedelta(days=i),
                    status = random.choice(["Absent", "Late", "Present"])
                )
        self.stdout.write(self.style.SUCCESS('Attendance records created.'))
            



        #Create Performance Records 
        for emp in employees:
            for _ in range(random.randint(1, 3)):
                Performance.objects.create(
                    employee= emp, 
                    rating = random.randint(1, 5), 
                    date=faker.date_between(start_date='-1y', end_date='today')
                )
        self.stdout.write(self.style.SUCCESS('Performance records created.'))