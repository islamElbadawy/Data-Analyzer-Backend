from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    country = models.CharField(max_length=255)
    salary = models.IntegerField()
    department = models.CharField(max_length=255)