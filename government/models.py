from django.db import models


# Create your models here.
class Citizen(models.Model):
    SEX = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.IntegerField()
    national_id = models.IntegerField()
    address = models.CharField(max_length=255)
    image_1 = models.ImageField()
    image_2 = models.ImageField()
    image_3 = models.ImageField()
    image_4 = models.ImageField()
    image_5 = models.ImageField()


