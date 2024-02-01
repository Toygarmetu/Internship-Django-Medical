from django.shortcuts import render
from .models import Doctor, Patient, Appointment, Medicine, Symptom

# Create your views here.


def index(request):
    doctors = Doctor.objects.all()
    return render(request, 'index.html', {'doctors': doctors})

