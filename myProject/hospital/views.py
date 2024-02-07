from django.shortcuts import render, redirect
from .models import Doctor, Patient, Appointment, Medicine, Symptom
from django.contrib.auth.decorators import login_required
from django.contrib import messages

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
        patient_id = request.POST.get('patient')
        status = request.POST.get('status')
        date = request.POST.get('date')
        time = request.POST.get('time')

        try:
            doctor = Doctor.objects.get(id=doctor_id)
            patient = Patient.objects.get(id=patient_id)
            appointment = Appointment.objects.create(
                doctor=doctor,
                patient=patient,
                status=status,
                date=date,
                time=time
            )
            messages.success(request, 'Appointment booked successfully.')
            return redirect('some_success_url')  # Redirect as appropriate
        except Exception as e:
            messages.error(request, 'Failed to book appointment. Error: {}'.format(e))

    else:
        doctors = Doctor.objects.all()
        patients = Patient.objects.all()
        return render(request, 'appointment.html', {'doctors': doctors, 'patients': patients})