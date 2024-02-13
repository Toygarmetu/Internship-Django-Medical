from django.contrib import admin
from .models import Doctor, Patient, Appointment, Medicine, Symptom, Specialization, MedicalCondition, Hospital, MedicalHistory
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class DoctorAdmin(admin.ModelAdmin):
    list_display = ('get_user', 'name', 'get_specialization', 'phone', 'email', 'office')
    search_fields = ('name', 'specialization__name', 'phone', 'email', 'office')

    def get_user(self, obj):
        # Check if the doctor has an associated user and return the username if so
        if obj.user:
            return obj.user.username
        return "No user associated"  # Return a placeholder or similar message if no user is associated

    get_user.short_description = 'Username'  # Sets column name

    def get_specialization(self, obj):
        # Returns a comma-separated list of specializations
        return ", ".join([s.name for s in obj.specialization.all()])
    get_specialization.short_description = 'Specialization'  # Sets column name

    def save_model(self, request, obj, form, change):
        if not obj.user_id:  # If the Doctor doesn't have a linked User instance yet
            # Assuming obj.email is intended for User creation, ensure uniqueness or handle potential conflicts.
            user, created = User.objects.get_or_create(email=obj.email, defaults={'username': obj.email})
            if created:
                user.set_password('defaultpassword')  # Consider a more secure approach
                user.save()
            obj.user = user
        super().save_model(request, obj, form, change)
    

admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Patient)
admin.site.register(Appointment)
admin.site.register(Medicine)
admin.site.register(Symptom)
admin.site.register(Specialization)
admin.site.register(MedicalCondition)
admin.site.register(Hospital)
admin.site.register(MedicalHistory)
