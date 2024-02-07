# pages/views.py
from django.http import HttpResponse
from django.shortcuts import render
from hospital.models import Doctor





def home(request):
    return render(request, 'home.html', { 'name': 'John' })

def doctors(request):
    doctors_list = Doctor.objects.all()
    return render(request, 'doctors.html', {'doctors': doctors_list})

