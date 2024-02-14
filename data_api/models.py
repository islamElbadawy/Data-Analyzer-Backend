from django.db import models

# Create your models here.
class Data(models.Model):
    Index = models.IntegerField()
    OrganizationId = models.CharField(max_length=255)
    Name = models.CharField(max_length=255)
    Website = models.URLField()
    Country = models.CharField(max_length=255)
    Description = models.TextField()
    Founded = models.IntegerField()
    Industry = models.CharField(max_length=255)
    NumberOfEmployees = models.IntegerField()