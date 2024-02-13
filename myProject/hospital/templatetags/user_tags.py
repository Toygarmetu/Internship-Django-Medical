from django import template
from ..models import Doctor, Patient  # Adjust this import based on your actual app name and structure

register = template.Library()

@register.filter(name='is_doctor')
def is_doctor(user):
    return Doctor.objects.filter(user=user).exists()

@register.filter(name='is_patient')
def is_patient(user):
    return Patient.objects.filter(user=user).exists()
