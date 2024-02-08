from django.shortcuts import render, redirect
from .models import Doctor, Patient, Appointment, Medicine, Symptom
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import datetime, time, timedelta
from .utils import time_slot, is_slot_available

# Create your views here.

@login_required(login_url='login')
def index(request):
    doctors = Doctor.objects.order_by('?')[:3]
    return render(request, 'index.html', {'doctors': doctors, 'user': request.user})

def about(request):
    return render(request, 'about.html')

def doctors(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctors.html', {'doctors': doctors})

def contact(request):
    return render(request, 'contact.html')

def hospitals(request):
    return render(request, 'hospitals.html')

@login_required
def book_appointment(request):
    if request.method == 'POST':
        doctor_id = request.POST.get('doctor')
        status = request.POST.get('status')
        date = request.POST.get('date')
        time = request.POST.get('time')
        try:
            doctor = Doctor.objects.get(id=doctor_id)
            patient = request.user.patient
            
            # Checking if the slot is available
            if not is_slot_available(doctor, date, time):
                messages.error(request, "This slot is already booked.")
                return redirect('appointment')  # Make sure to return here to prevent further execution
            
            # If the slot is available, proceed to create the appointment
            Appointment.objects.create(
                doctor=doctor,
                patient=patient,
                status=status,
                date=date,
                time=time
            )
            messages.success(request, 'Appointment booked successfully.')
            return redirect('/')  # Redirect as appropriate
        except Exception as e:
            messages.error(request, 'Failed to book appointment. Error: {}'.format(e))
            return redirect('appointment')  # Make sure to return here as well

    doctors = Doctor.objects.all()
    return appointment_view(request, doctors)


@login_required
def appointment_view(request, doctors):
    start_time = time(9, 0)  
    end_time = time(16, 45)  
    interval = timedelta(minutes=15)  

    time_slots = Appointment.objects.generate_time_slots(start_time, end_time, interval)
    doctor = Doctor.objects.get(pk=1)  
    date = datetime.today().date()  
    available_slots = [slot for slot in time_slots if Appointment.objects.is_slot_available(doctor, date, slot[0])]



    return render(request, 'appointment.html', {'time_slots': available_slots, 'doctors': doctors})