from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    gender = models.CharField(max_length=100)
    age = models.CharField(max_length=100)

    def __str__(self):
        return self.name
