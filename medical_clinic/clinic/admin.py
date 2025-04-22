from django.contrib import admin
from . models import Doctor, Patient, LabTechnician, Pharmacist, Appointment, Sample, Medical_Condition, Diagnose, Pill, Prescription

# Customize admin site
admin.site.site_header = "Medical Clinic Administration"  # Changes the "Django administration" text
admin.site.site_title = "Medical Clinic Admin Portal"     # Changes the browser tab title
admin.site.index_title = "Welcome to Medical Clinic Admin Portal"  # Changes the header on the main admin index page

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['healthcare_number', 'emergency_contact']
    search_fields = ['healthcare_number', 'emergency_contact']
    raw_id_fields = ['user']

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['healthcare_number','specialty', 'license_number']
    search_fields = ['healthcare_number','specialty', 'license_number']
    raw_id_fields = ['user']

@admin.register(LabTechnician)
class LabTechnicianAdmin(admin.ModelAdmin):
    list_display = ['healthcare_number', 'specialization', 'certification']
    search_fields = ['healthcare_number', 'specialization', 'certification']
    raw_id_fields = ['user']

@admin.register(Pharmacist)
class PharmacistAdmin(admin.ModelAdmin):
    list_display = ['healthcare_number', 'license_number', 'years_of_experience']
    search_fields = ['healthcare_number', 'license_number', 'years_of_experience']
    raw_id_fields = ['user']

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['doctor', 'patient', 'appointment_datetime']
    #search_fields = ['healthcare_number', 'license_number', 'years_of_experience']
    #raw_id_fields = ['user']

@admin.register(Medical_Condition)
class ConditionAdmin(admin.ModelAdmin):
    list_display = ['condition_name', 'condition_description']

@admin.register(Diagnose)
class DiagnoseAdmin(admin.ModelAdmin):
    list_display = ['appointment', 'condition', 'status_now']

@admin.register(Sample)
class SampleAdmin(admin.ModelAdmin):
    list_display = ['patient', 'sample_type', 'obtained_date', 'technician']

@admin.register(Pill)
class PillAdmin(admin.ModelAdmin):
    list_display = ['pill_name', 'pill_description']

@admin.register(Prescription)
class PrescriptionAdmin(admin.ModelAdmin):
    list_display = ['appointment', 'pill', 'pharmacist', 'pill_count', 'pill_refills', 'concentration', 'instructions', 'created']

