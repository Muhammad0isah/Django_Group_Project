from typing import Sized
from django import forms
from django.db import models
from django.forms import widgets


# Create your models here.
class CustormerDetail(models.Model):
    full_name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.full_name

    username = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(max_length=200)
    address = models.CharField(max_length=255)
    password = models.CharField(max_length=50)
    confirm_password = models.CharField(max_length=50)
