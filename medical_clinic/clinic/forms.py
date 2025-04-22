from django import forms
from .models import Patient, Appointment

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