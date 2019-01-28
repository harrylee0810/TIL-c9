from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.TextField()
    uni = models.CharField(max_length=100)
# Create your models here.
