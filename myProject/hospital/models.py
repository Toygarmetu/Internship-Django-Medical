from django.db import models
from django.contrib.auth.models import User
from .utils import time_slot, is_slot_available
from datetime import time, timedelta

# Create your models here.

class Specialization(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    
    
class MedicalCondition(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    branch = models.TextField()
    specialization = models.ManyToManyField('Specialization')
    phone = models.CharField(max_length=20) 
    email = models.EmailField() 
    office = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images', default='default_doctor.jpg')

    def __str__(self):
        return self.name

# And for Patient:
class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)  
    email = models.EmailField()  
    gender = models.CharField(max_length=100)
    age = models.IntegerField(null=True)  
    address = models.CharField(max_length=100)
    illness = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    
class AppointmentManager(models.Manager):
    def generate_time_slots(self, start_time, end_time, interval):
        return [(slot, slot) for slot in time_slot(start_time, end_time, interval)]

    def is_slot_available(self, doctor, date, time):
        return is_slot_available(doctor, date, time)

class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    status = models.CharField(max_length=100, default='pending', editable=True)
    date = models.DateField()
    time = models.TimeField()
    updated_at = models.DateTimeField(auto_now=True)

    objects = AppointmentManager()


def __str__(self):
    return self.doctor.name + ' - ' + self.patient.name

class Medicine(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    expiry_date = models.DateField()
    dosage = models.CharField(max_length=100)
    price = models.IntegerField()
    quantity = models.IntegerField()
    

def __str__(self):
    return self.name

class Symptom(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    severity = models.CharField(max_length=100)
    commonness = models.CharField(max_length=100)
    related_diseases = models.ManyToManyField('MedicalCondition')
    possible_treatment = models.CharField(max_length=100)
    

def __str__(self):
    return self.name

class Hospital(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    website = models.URLField()
    image = models.ImageField(upload_to='images', default='default_hospital.jpg')
    

def __str__(self):
    return self.name
