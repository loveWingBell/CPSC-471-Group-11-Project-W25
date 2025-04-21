from django import forms
from .models import Patient

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