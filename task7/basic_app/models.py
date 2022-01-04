from django.db import models
from django.db.models.base import Model

# Create your models here.


class School(models.Model):
    name = models.CharField(max_length=256)
    pricipal = models.CharField(max_length=50)
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    school = models.ForeignKey(School, related_name = 'students', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    