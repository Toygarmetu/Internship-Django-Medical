from django.db import models

# Create your models here.

class Specialization(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

    
    
    
class MedicalCondition(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    symptoms = models.ManyToManyField('Symptom')
    
    def __str__(self):
        return self.name

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    branch = models.TextField(max_length=100)
    specialization = models.ManyToManyField(Specialization)
    phone = models.IntegerField(max_length=20)
    email = models.CharField(max_length=100)
    office = models.CharField(max_length=100)
    #img = models.ImageField(upload_to='pics')

    #img = models.ImageField(upload_to='pics')

#     def __str__(self):
#         return self.name

class Patient(models.Model):
    name = models.CharField(max_length=100)
    phone = models.IntegerField(max_length=20)
    email = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    age = models.IntegerField(max_length=20)
    address = models.CharField(max_length=100)
    illness = models.CharField(max_length=100)
    
    #img = models.ImageField(upload_to='pics')

    #img = models.ImageField(upload_to='pics')
    

def __str__(self):
    return self.name

class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    status = models.CharField(max_length=100, default='pending', editable=True)
    date = models.DateField()
    time = models.TimeField()
    updated_at = models.DateTimeField(auto_now=True)
    


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
