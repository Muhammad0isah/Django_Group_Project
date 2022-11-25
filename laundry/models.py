from os import name
from django.db import models
from django.db.models.deletion import CASCADE


# Create your models here.
class Record(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

    phone_number = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    Area_list = (
        ('Dala', 'Dala'),
        ('Nasarawa', 'Nasarawa'),
        ('Fagge', 'Fagge'),
        ('Bichi', 'Bichi'),
        ('Kano Municipal', 'Kano Municipal'),
    )
    area = models.CharField(choices=Area_list, max_length=30)
    state_list = (
        ('Kano', 'Kano'),
    )
    city = models.CharField(choices=state_list, max_length=40)
