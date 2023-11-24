from django.db import models

class Member(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    phone = models.IntegerField(null=True)
    joined_date = models.DateField(null=True)

    def __str__(self):
       return self.firstName
    