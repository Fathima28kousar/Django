from django.db import models

class Car(models.Model):
    car_name = models.CharField(max_length=100)
    speed = models.IntegerField(default=50)

    def __str__(self):
        return self.car_name
