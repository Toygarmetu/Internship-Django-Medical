from django.db import models

class Specialization(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    branch = models.TextField(max_length=100)
    specialization = models.ManyToManyField(Specialization)
    phone = models.IntegerField(max_length=20)
    email = models.CharField(max_length=100)
    office = models.CharField(max_length=100)
    
    
