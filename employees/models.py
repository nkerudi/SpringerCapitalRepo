from django.db import models

# Department model with name field (foreign key)
class Department(models.Model):
    name = models.CharField(max_length=100)
    
    #string representation
    def __str__(self):
        return self.name
    
#Employee Model
#with name, email, phone, address, date of joining, and department fields 
class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique = True)
    phone = models.CharField(max_length=40)
    address = models.TextField()
    date_of_joining = models.DateField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

#return string representation 
    def __str__(self):
        return self.name