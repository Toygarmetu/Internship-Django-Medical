# pages/views.py
from django.http import HttpResponse
from django.shortcuts import render





def home(request):
    return render(request, 'home.html', { 'name': 'John' })

def doctors(request):
    return render(request, 'doctors.html')

