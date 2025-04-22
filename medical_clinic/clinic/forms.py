from django import forms
from .models import Patient, Appointment, Sample, Prescription, Diagnose

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ('healthcare_number', 'birthday', 'gender', 'insurance', 'phone_number', 'address', 'user', 'emergency_contact')
        
        widgets = {
            'healthcare_number': forms.TextInput(attrs={'class': 'form-control'}),
            'birthday': forms.DateInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'insurance': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control'}),
            'user': forms.Select(attrs={'class': 'form-control'}),
            'emergency_contact': forms.TextInput(attrs={'class': 'form-control'})
        }

class EditPatientForm(forms.ModelForm):
    """ Doctor can edit patient profile"""
    class Meta:
        model = Patient
        fields = ('healthcare_number', 'birthday', 'gender', 'insurance', 'phone_number', 'address', 'user', 'emergency_contact')
         
        widgets = {
            'healthcare_number': forms.TextInput(attrs={'class': 'form-control'}),
            'birthday': forms.DateInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'insurance': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control'}),
            'user': forms.Select(attrs={'class': 'form-control'}),
            'emergency_contact': forms.TextInput(attrs={'class': 'form-control'})
            }

class DoctorAddAppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ('patient', 'appointment_datetime', 'reason_for_visit', 'observations')
        
        widgets = {
            #'doctor': forms.Select(attrs={'class': 'form-control'}),
            'patient': forms.Select(attrs={'class': 'form-control'}),
            'appointment_datetime': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'reason_for_visit': forms.TextInput(attrs={'class': 'form-control'}),
            'observations': forms.Textarea(attrs={'class': 'form-control'}),
        }

class DoctorUpdateAppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ('doctor','patient', 'appointment_datetime', 'reason_for_visit', 'observations')
        
        widgets = {
            'doctor': forms.Select(attrs={'class': 'form-control'}),
            'patient': forms.Select(attrs={'class': 'form-control'}),
            'appointment_datetime': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'reason_for_visit': forms.TextInput(attrs={'class': 'form-control'}),
            'observations': forms.Textarea(attrs={'class': 'form-control'}),
        }

class PatientAddAppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ('doctor', 'appointment_datetime', 'reason_for_visit', 'observations')
        
        widgets = {
            'doctor': forms.Select(attrs={'class': 'form-control'}),
            #'patient': forms.Select(attrs={'class': 'form-control'}),
            'appointment_datetime': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'reason_for_visit': forms.TextInput(attrs={'class': 'form-control'}),
            'observations': forms.Textarea(attrs={'class': 'form-control'}),
        }

class PatientUpdateAppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ('doctor', 'appointment_datetime', 'reason_for_visit', 'observations')
        
        widgets = {
            'doctor': forms.Select(attrs={'class': 'form-control'}),
            #'patient': forms.Select(attrs={'class': 'form-control'}),
            'appointment_datetime': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'reason_for_visit': forms.TextInput(attrs={'class': 'form-control'}),
            'observations': forms.Textarea(attrs={'class': 'form-control'}),
        }

class SampleForm(forms.ModelForm):
    class Meta:
        model = Sample
        fields = ('patient', 'sample_type', 'obtained_date', 'technician')
        
        widgets = {
            'patient': forms.Select(attrs={'class': 'form-control'}),
            'sample_type': forms.Select(attrs={'class': 'form-control'}),
            'obtained_date': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'technician': forms.Select(attrs={'class': 'form-control'})
        }

class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = ('appointment', 'pill', 'pharmacist', 'pill_count', 'pill_refills', 'concentration', 'instructions', 'created')
        
        widgets = {
            'appointment': forms.Select(attrs={'class': 'form-control'}),
            'pill': forms.Select(attrs={'class': 'form-control'}),
            'pharmacist': forms.Select(attrs={'class': 'form-control'}),
            'pill_count': forms.NumberInput(attrs={'class': 'form-control'}),
            'pill_refills': forms.NumberInput(attrs={'class': 'form-control'}),
            'concentration': forms.NumberInput(attrs={'class': 'form-control'}),
            'instructions': forms.Select(attrs={'class': 'form-control'}),
            'created': forms.DateInput(attrs={'class': 'form-control'})
        }

class DiagnoseForm(forms.ModelForm):
    class Meta:
        model = Diagnose
        fields = ('appointment', 'condition', 'status_now')
        
        widgets = {
            'appointment': forms.Select(attrs={'class': 'form-control'}),
            'condition': forms.Select(attrs={'class': 'form-control'}),
            'status_now': forms.NullBooleanSelect(attrs={'class': 'form-control'})
        }
