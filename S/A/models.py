from django.db import models


class Department(models.Model):
    department = models.CharField(max_length=100)
    
    def __str__(self):
        return self.department
    
    class Meta:
        ordering = ['department']

class StudentID(models.Model):
    student_id = models.CharField(max_length=100)

    def __str__(self):
        return self.student_id
    
class Student(models.Model):
    department = models.ForeignKey(Department,related_name="depart",on_delete=models.CASCADE)
    student_id = models.OneToOneField(StudentID,related_name="studentid",on_delete=models.CASCADE)
    student_name = models.CharField(max_length=100)
    student_email = models.EmailField(unique=True)
    student_age = models.IntegerField(default=18)
    student_address = models.TextField()

    def __str__(self):
        return self.student_name
    
    class Meta:
        ordering = ['student_name']
        verbose_name = "student"

class Employee(models.Model):
    ename = models.TextField(max_length=100)
    email = models.EmailField()
    esal = models.FloatField()
    eaddress = models.TextField()
    
class Car(models.Model):
    car_name = models.TextField(max_length=500)
    car_speed = models.IntegerField()
    car_price = models.IntegerField()
    car_description = models.TextField()
    car_image = models.ImageField(upload_to="car")
