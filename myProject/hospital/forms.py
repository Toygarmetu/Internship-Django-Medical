from django import forms
from .models import MedicalHistory, Patient, Symptom

class MedicalHistoryForm(forms.ModelForm):
    class Meta:
        model = MedicalHistory
        fields = ['condition', 'description', 'date_diagnosed', 'treatment', 'outcome']
        
class PatientProfileForm(forms.ModelForm):
    symptoms = forms.ModelMultipleChoiceField(queryset=Symptom.objects.all(), widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = Patient
        fields = ['email', 'phone', 'address', 'age', 'gender', 'symptoms']

