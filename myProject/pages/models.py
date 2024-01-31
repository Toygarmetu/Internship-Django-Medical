from django.db import models

# Create your models here.


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
    #img = models.ImageField(upload_to='pics')
    

    

# class Patient(models.Model):
#     name = models.CharField(max_length=100)
    
# class Doctor(models.Model):
#     name = models.CharField(max_length=100)
#     patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    
# class Medicine(models.Model):
#     name = models.CharField(max_length=100)
#     patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
#     doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
#     hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)

# class Symptom(models.Model):
#     name = models.CharField(max_length=100)
#     patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
#     doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
#     hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
#     medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    
# class Disease(models.Model):
#     name = models.CharField(max_length=100)
#     patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
#     doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
#     hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
#     medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
#     symptom = models.ForeignKey(Symptom, on_delete=models.CASCADE)
    

