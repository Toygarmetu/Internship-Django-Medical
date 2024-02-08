from django.contrib import admin
from .models import Doctor, Patient, Appointment, Medicine, Symptom, Specialization, MedicalCondition, Hospital
# Register your models here.

class DoctorAdmin(admin.ModelAdmin):
    filter_horizontal = ('specialization',)

admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Patient)
admin.site.register(Appointment)
admin.site.register(Medicine)
admin.site.register(Symptom)
admin.site.register(Specialization)
admin.site.register(MedicalCondition)
admin.site.register(Hospital)