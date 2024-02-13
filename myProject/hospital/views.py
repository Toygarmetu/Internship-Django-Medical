from django.shortcuts import render, redirect
from .models import Doctor, Patient, Appointment, Medicine, Symptom, Specialization, MedicalCondition, Hospital, Symptom, MedicalHistory, Prescription
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import datetime, time, timedelta
from .utils import time_slot, is_slot_available
from .forms import MedicalHistoryForm
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .forms import PatientProfileForm

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
    hospitals = Hospital.objects.all()
    return render(request, 'hospitals.html', {'hospitals': hospitals})

def medicines(request):
    medicines = Medicine.objects.all()
    return render(request, 'medicines.html', {'medicines': medicines})

def symptoms(request):
    symptoms = Symptom.objects.all()
    return render(request, 'symptoms.html', {'symptoms': symptoms})

def diseases(request):
    diseases = MedicalCondition.objects.all()
    return render(request, 'diseases.html', {'diseases': diseases})

def patient_profile(request, patient_id):
    patient = get_object_or_404(Patient, pk=patient_id)
    medical_histories = MedicalHistory.objects.filter(patient=patient)
    symptoms = Symptom.objects.all()
    return render(request, 'patient_profile.html', {'patient': patient, 'medical_histories': medical_histories, 'symptoms': symptoms})

def doctor_profile(request, doctor_id):
    doctor = get_object_or_404(Doctor, pk=doctor_id)
    return render(request, 'doctor_profile.html', {'doctor': doctor, 'user': request.user})



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


def add_medical_history(request, patient_id):
    patient = get_object_or_404(Patient, pk=patient_id)
    if request.method == 'POST':
        form = MedicalHistoryForm(request.POST)
        if form.is_valid():
            medical_history = form.save(commit=False)
            medical_history.patient = patient
            medical_history.save()
            
            return redirect('patient_profile', patient_id=patient.id)
    else:
        form = MedicalHistoryForm()

    return render(request, 'add_medical_history.html', {'form': form})


def submit_prescription(request):
    medicines = Medicine.objects.all()
    if request.method == "POST":
        # Extract form data
        patient_name = request.POST.get('patientName')
        patient_id = request.POST.get('patientID')
        date = request.POST.get('date')
        medication = request.POST.get('medication')
        dosage = request.POST.get('dosage')
        instructions = request.POST.get('instructions')

        # Process and save the prescription data
        # This is just an example, adapt it to your models and logic
        Prescription.objects.create(
            patient_name=patient_name,
            patient_id=patient_id,
            date=date,
            medication=medication,
            dosage=dosage,
            instructions=instructions
        )
        return redirect('doctor_profile',  {{'medicines': medicines}} , doctor_id=request.user.doctor.id) 
        

    
@login_required
def update_patient_profile(request, patient_id):
    patient = get_object_or_404(Patient, pk=patient_id)
    if request.method == "POST":
        form = PatientProfileForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('patient_profile', patient_id=patient.id)
    else:
        form = PatientProfileForm(instance=patient)
    return render(request, 'patient_profile.html', {'form': form, 'patient': patient})