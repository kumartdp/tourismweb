from django.db import models


class Student(models.Model):
    firstname=models.CharField(max_length=32)
    email=models.CharField(max_length=32)

# Create your models here.
