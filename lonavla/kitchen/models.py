from django.db import models

class Dish(models.Model):
    dish_name = models.CharField(max_length=500)
    dish_description = models.TextField()
    dish_image = models.ImageField(upload_to="dish")
